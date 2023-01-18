from typing import List
from bson.objectid import ObjectId

from db.client import db
from db.serializers.link_serializer import link_entity, links_entity
from schemas.user import User
from schemas.link import Link, LinkInDB


links = db.get_collection("links")


def get_by_id(id: str, user: User) -> LinkInDB:
    try:
        link = links.find_one({ "_id": ObjectId(id), "user.id": user.id })
    except:
        return None
    
    if link is None:
        return None
    
    return link_entity(link)


def get_all(user: User) -> List[LinkInDB]:
    return links_entity(links.find({ "user.id": user.id  }))


def add(link: Link, user: User) -> LinkInDB:
    inserted = links.insert_one(link.dict())
    inserted_id = inserted.inserted_id
    return get_by_id(id=inserted_id, user=user)


def delete(id: str, user: User) -> LinkInDB:
    link: LinkInDB = get_by_id(id=id, user=user)

    if link is None:
        return None
    
    try:
        links.delete_one({ "_id": ObjectId(id), "user.id": user.id })
    except:
        return None
    
    return link
