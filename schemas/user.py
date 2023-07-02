from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[str]
    username: str
    email: EmailStr


class UserIn(User):
    password: str


class UserInDB(User):
    hashed_password: str


class UserResponse(User):
    pass
