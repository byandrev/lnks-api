from typing import Union
from fastapi import APIRouter, Depends, status

import db.repository.links_repository as repository
from core.auth import get_current_user
from schemas.custom_exception import CustomException
from schemas.link import Link, LinkInDB
from schemas.response import Response
from schemas.user import User


router = APIRouter(prefix="/links")


@router.get("/", response_model=Response, status_code=status.HTTP_200_OK)
def get_all_links(user: User = Depends(get_current_user)):
    links = repository.get_all(user)

    if links is None:
        raise CustomException(
            status=status.HTTP_404_NOT_FOUND,
            error="No links"
        )

    return Response(status=status.HTTP_200_OK, body=links, msg="All links")


@router.get("/{id}", response_model=Response, status_code=status.HTTP_200_OK)
def get_by_id(id: str, user: User = Depends(get_current_user)):
    link: Union[LinkInDB, None] = repository.get_by_id(id=id, user=user)

    if link is None:
        raise CustomException(
            status=status.HTTP_404_NOT_FOUND,
            error="No found the link"
        )

    return Response(status=status.HTTP_200_OK, body=link, msg="Link by id")


@router.post("/", response_model=Response, status_code=status.HTTP_201_CREATED)
def create_link(link: Link, user: User = Depends(get_current_user)):
    created_link: Union[LinkInDB, None] = repository.add(link=link, user=user)

    if created_link is None:
        raise CustomException(
            status=status.HTTP_400_BAD_REQUEST,
            error="No created the link"
        )

    return Response(status=status.HTTP_201_CREATED, body=created_link, msg="Link created")


@router.delete("/{id}", response_model=Response, status_code=status.HTTP_200_OK)
def delete_link(id: str, user: User = Depends(get_current_user)):
    deleted_link = repository.delete(id, user=user)

    if deleted_link is None:
        raise CustomException(
            status=status.HTTP_404_NOT_FOUND,
            error="No found the link"
        )

    return Response(status=status.HTTP_200_OK, body=deleted_link, msg="Link deleted")
