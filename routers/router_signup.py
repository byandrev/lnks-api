from fastapi import APIRouter, HTTPException, status

import db.repository.users_repository as repository
from schemas.user import UserIn, UserResponse
from core.security import create_access_token, decode_token


router = APIRouter(prefix="/signup", tags=["auth", "signup"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def sign_up(user: UserIn) -> any:
    user_created: UserResponse = repository.add(user)
    
    if user_created is not None:
        return user_created
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")
    
    """
    user: UserInDB = get_user(username="tests@gmail.com")

    if user is not None:
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")
    """
