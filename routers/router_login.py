from typing import Union
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError

from core.hashing import Hasher
from core.security import create_access_token, decode_token
from schemas.token import Token
from schemas.user import UserInDB, UserResponse
from db.repository.users_repository import get_user


router = APIRouter(prefix="/login", tags=["auth", "login"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = decode_token(token)
        username: str = payload.get("sub")
        
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user: UserResponse = get_user(username=username)
    
    if user is None:
        raise credentials_exception
    
    return user


def authenticate_user(username: str, password: str) -> Union[UserResponse, bool]:
    user: UserInDB = get_user(username=username)
    
    if not user:
        return False
    if not Hasher.verify_password(password, user["hashed_password"]):
        return False

    return user


@router.post("/", response_model=Token, status_code=status.HTTP_200_OK)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token({ "sub": user["email"] })
    
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_me(user: UserResponse = Depends(get_current_user)):
    return user
