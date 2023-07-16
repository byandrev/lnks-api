from typing import Union
from fastapi import APIRouter, HTTPException, status

import db.repository.users_repository as repository
from schemas.response import Response
from schemas.user import UserIn, UserInDB, UserResponse

router = APIRouter(prefix="/signup", tags=["auth", "signup"])


@router.post("/", response_model=Response, status_code=status.HTTP_201_CREATED)
def sign_up(user: UserIn):
    user_exist: Union[UserInDB, None] = repository.get_user(user.email)

    if user_exist is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist")

    user_created: Union[UserResponse, None] = repository.add(user)

    if user_created is not None:
        return Response(status=status.HTTP_201_CREATED, body=UserResponse(**user_created),
                        msg="User created successfully")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")
