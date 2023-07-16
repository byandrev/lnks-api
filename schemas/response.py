from typing import Optional, Any

from pydantic import BaseModel


class Response(BaseModel):
    msg: Optional[str] = None
    status: int
    body: Optional[Any] = None
    error: Optional[str] = None
