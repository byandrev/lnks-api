from typing import List

from schemas.link import Link


def link_entity(link) -> dict:
    return {
        "id": str(link["_id"]),
        "url": link["url"],
        "user": link["user"],
        "tags": link["tags"]
    }


def links_entity(links) -> List[dict]:
    return [link_entity(link) for link in links]
