from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

from practice.phase02.db import (
    find_member_by_email,
    get_connection,
    insert_member as execute_member_insert,
)


app = FastAPI()


class MemberCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=0, le=150)


class MemberResponse(MemberCreate):
    id: int


def check_duplicate_email(email: str):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            return find_member_by_email(cursor, email)


def validate_duplicate_email(email: str):
    existing = check_duplicate_email(email)

    if existing:
        raise HTTPException(
            status_code=409,
            detail="이미 등록된 이메일입니다.",
        )


@app.post(
    "/members",
    response_model=MemberResponse,
    status_code=201,
)
def create_member(member: MemberCreate):
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            existing = find_member_by_email(cursor, str(member.email))

            if existing:
                raise HTTPException(
                    status_code=409,
                    detail="이미 등록된 이메일입니다.",
                )

            execute_member_insert(
                cursor,
                member.name,
                str(member.email),
                member.age,
            )
            row = cursor.fetchone()
            conn.commit()

            return {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "age": row[3],
            }
    except HTTPException:
        conn.rollback()
        raise
    except Exception:
        conn.rollback()
        raise HTTPException(
            status_code=500,
            detail="회원 등록 중 오류가 발생했습니다.",
        )
    finally:
        conn.close()
