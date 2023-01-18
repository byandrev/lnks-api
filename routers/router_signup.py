from typing import Union
from fastapi import APIRouter, HTTPException, status

import db.repository.users_repository as repository
from schemas.user import UserIn, UserResponse
from core.security import create_access_token, decode_token


router = APIRouter(prefix="/signup", tags=["auth", "signup"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def sign_up(user: UserIn):
    user_created: Union[UserResponse, None] = repository.add(user)

    if user_created is not None:
        return user_created

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

