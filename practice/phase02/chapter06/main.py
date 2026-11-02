from fastapi import FastAPI
from pydantic import BaseModel
from database import fetch_members

app = FastAPI()

class MemberResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

@app.get("/members", response_model=list[MemberResponse])
def get_members():
    rows = fetch_members()
    members = []
    for row in rows:
        members.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "age": row[3]
        })
    return members

