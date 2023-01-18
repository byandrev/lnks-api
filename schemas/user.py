import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    id: Optional[str]
    username: str
    email: EmailStr


class UserIn(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


class UserResponse(UserBase):
    pass
