from typing import Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from core.hashing import Hasher
from core.security import decode_token
from db.repository.users_repository import get_user
from schemas.user import UserInDB, User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
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
    
    user: User = User(**get_user(username=username))
    
    if user is None:
        raise credentials_exception
    
    return user


def authenticate_user(username: str, password: str) -> Union[User, bool]:
    user: UserInDB = UserInDB(**get_user(username=username))
    
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False

    return User(**user.dict())
