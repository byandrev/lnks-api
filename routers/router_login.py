from typing import Union
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from core.security import create_access_token
from core.auth import authenticate_user, get_current_user
from schemas.custom_exception import CustomException
from schemas.response import Response
from schemas.token import Token
from schemas.user import User, UserResponse

router = APIRouter(prefix="/login", tags=["auth", "login"])


@router.post("/", response_model=Response, status_code=status.HTTP_200_OK)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: Union[User, bool] = authenticate_user(
        form_data.username, form_data.password)

    if not user:
        raise CustomException(
            status=status.HTTP_401_UNAUTHORIZED,
            error="Incorrect username or password"
        )

    access_token = create_access_token({"sub": user.email})

    token = Token(access_token=access_token, token_type="bearer")
    return Response(status=status.HTTP_200_OK, body=token, msg="Login successful")


@router.get("/me", response_model=Response, status_code=status.HTTP_200_OK)
def get_me(user: UserResponse = Depends(get_current_user)):
    return Response(status=status.HTTP_200_OK, body=user, msg="User data")
