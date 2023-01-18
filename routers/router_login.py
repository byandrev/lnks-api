from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from core.security import create_access_token
from core.auth import authenticate_user, get_current_user
from schemas.token import Token
from schemas.user import User, UserResponse


router = APIRouter(prefix="/login", tags=["auth", "login"])


@router.post("/", response_model=Token, status_code=status.HTTP_200_OK)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: User = authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token({ "sub": user.email })
    
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_me(user: UserResponse = Depends(get_current_user)):
    return user
