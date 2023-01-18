from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

import db.repository.links_repository as repository
from core.auth import get_current_user
from schemas.link import Link, LinkResponse
from schemas.user import User


router = APIRouter(prefix="/links")


@router.get("/", response_model=List[LinkResponse], status_code=status.HTTP_200_OK)
def get_all_links(user: User = Depends(get_current_user)):
    users = repository.get_all(user)
    
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return users


@router.get("/{id}", response_model=LinkResponse, status_code=status.HTTP_200_OK)
def get_by_id(id: str, user: User = Depends(get_current_user)):
    user = repository.get_by_id(id=id, user=user)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return user
    

@router.post("/", response_model=LinkResponse, status_code=status.HTTP_201_CREATED)
def create_link(link: Link, user: User = Depends(get_current_user)):
    return repository.add(link, user=user)


@router.delete("/{id}", response_model=LinkResponse, status_code=status.HTTP_200_OK)
def delete_link(id: str, user: User = Depends(get_current_user)):
    deleted_link = repository.delete(id, user=user)
    
    if deleted_link is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No exist the link"
        )
        
    return deleted_link
    