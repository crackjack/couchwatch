from pydantic import BaseModel, HttpUrl
from typing import Optional


class BaseEntry(BaseModel):
    netflix_id: Optional[str] = None
    name: str


class CreateEntry(BaseEntry):
    pass


class Entry(BaseEntry):
    netflix_url: HttpUrl

    class Config:
        orm_mode = True
