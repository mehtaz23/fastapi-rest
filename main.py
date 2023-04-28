from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("788912a5-f6cc-471c-a1a4-5d9af917e6df"), #id=uuid4()
        first_name="LeBron", 
        last_name="James", 
        middle_name="Raymone", 
        gender=Gender.male, 
        roles=[Role.admin]
    ),
    User(
        id=UUID("ea42fed9-485c-4120-aab4-e414885efb71"), #id=uuid4()
        first_name="Sue",
        last_name="Bird",
        gender=Gender.female,
        roles=[Role.student, Role.user]
    )
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
