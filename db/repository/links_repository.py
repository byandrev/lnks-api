from typing import List, Union
from bson.objectid import ObjectId

from db.client import db
from db.serializers.link_serializer import link_entity, links_entity
from schemas.user import User
from schemas.link import Link, LinkInDB


links = db.get_collection("links")


def get_by_id(id: str, user: User) -> Union[LinkInDB, None]:
    try:
        link = links.find_one({ "_id": ObjectId(id), "user.id": user.id })
    except:
        return None
    
    if link is None:
        return None


    return LinkInDB(**link_entity(link))


def get_all(user: User) -> List[LinkInDB]:
    return [LinkInDB(**link) for link in links_entity(links.find({ "user.id": user.id  }))]


def add(link: Link, user: User) -> Union[LinkInDB, None]:
    to_insert = link.dict()
    to_insert.update({ "user": user.dict() })
    
    inserted = links.insert_one(to_insert)
    inserted_id = inserted.inserted_id
    return get_by_id(id=inserted_id, user=user)


def delete(id: str, user: User) -> Union[LinkInDB, None]:
    link: Union[LinkInDB, None] = get_by_id(id=id, user=user)

    if link is None:
        return None

    try:
        links.delete_one({ "_id": ObjectId(id), "user.id": user.id })
    except:
        return None

    return link

