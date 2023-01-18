from typing import List, Optional
from pydantic import BaseModel

from schemas.user import User


class Link(BaseModel):
    url: str
    user: Optional[User]
    tags: Optional[List[str]] = None


class LinkIn(Link):
    pass


class LinkInDB(Link):
    id: str


class LinkResponse(Link):
    id: str
