from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException

import db.repository.links_repository as repository
from core.auth import get_current_user
from schemas.link import Link, LinkInDB, LinkResponse
from schemas.user import User


router = APIRouter(prefix="/links")


@router.get("/", response_model=List[LinkResponse], status_code=status.HTTP_200_OK)
def get_all_links(user: User = Depends(get_current_user)):
    links = repository.get_all(user)

    if links is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return links


@router.get("/{id}", response_model=LinkResponse, status_code=status.HTTP_200_OK)
def get_by_id(id: str, user: User = Depends(get_current_user)):
    user: Union[LinkInDB, None] = repository.get_by_id(id=id, user=user)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user


@router.post("/", response_model=LinkResponse, status_code=status.HTTP_201_CREATED)
def create_link(link: Link, user: User = Depends(get_current_user)):
    created_link: Union[LinkInDB, None] = repository.add(link=link, user=user)
    
    if created_link is None:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No created the link"
        )

    return created_link


@router.delete("/{id}", response_model=LinkResponse, status_code=status.HTTP_200_OK)
def delete_link(id: str, user: User = Depends(get_current_user)):
    deleted_link = repository.delete(id, user=user)

    if deleted_link is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No exist the link"
        )

    return deleted_link

