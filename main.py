from typing import Optional, List

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/api/users")
async def get_users():
    return users


@app.post("/api/users", response_model=List[User])
async def create_user(user: User):
    users.append(user)
    return "success"


@app.get("api/users/{id}")
async def get_user(id: int = Path(..., description="The id of the user you want to retrieve")):
    return users[id]

# @app.delete("api/users/{id}")
# def delete_user(id: int):
#     users.f
#     users.remove(id)
