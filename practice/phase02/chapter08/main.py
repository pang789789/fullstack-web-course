from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, model_validator
from psycopg.rows import dict_row

from practice.phase02.db import get_connection


app = FastAPI()


class MemberResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int


class MemberPatch(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    age: int | None = Field(default=None, ge=0, le=150)

    @model_validator(mode="after")
    def reject_explicit_null(self):
        for field in self.model_fields_set:
            if getattr(self, field) is None:
                raise ValueError(f"{field} cannot be null")
        return self


@app.patch("/members/{member_id}", response_model=MemberResponse)
def patch_member(member_id: int, member: MemberPatch):
    changes = member.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(
            status_code=400,
            detail="At least one field is required",
        )

    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT id FROM members WHERE id = %s",
                (member_id,),
            )
            if cur.fetchone() is None:
                raise HTTPException(status_code=404, detail="Member not found")

            if "email" in changes:
                cur.execute(
                    """
                    SELECT id
                    FROM members
                    WHERE email = %s AND id <> %s
                    """,
                    (str(changes["email"]), member_id),
                )
                if cur.fetchone() is not None:
                    raise HTTPException(status_code=409, detail="Email already exists")

            allowed_fields = {
                "name": "name",
                "email": "email",
                "age": "age",
            }
            set_parts = []
            values = []

            for field, value in changes.items():
                column = allowed_fields[field]
                set_parts.append(f"{column} = %s")
                values.append(str(value) if field == "email" else value)

            values.append(member_id)
            sql = f"""
                UPDATE members
                SET {', '.join(set_parts)}
                WHERE id = %s
                RETURNING id, name, email, age
            """

            cur.execute(sql, values)
            updated = cur.fetchone()
            conn.commit()
            return updated


@app.get("/members/{member_id}", response_model=MemberResponse)
def get_member(member_id: int):
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                SELECT id, name, email, age
                FROM members
                WHERE id = %s
                """,
                (member_id,),
            )
            member = cur.fetchone()

    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")

    return member
