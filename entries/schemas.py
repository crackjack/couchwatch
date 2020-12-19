from pydantic import BaseModel
from typing import Optional


class BaseEntry(BaseModel):
    name: str


class CreateEntry(BaseEntry):
    netflix_id: Optional[str] = None


class Entry(BaseEntry):

    class Config:
        orm_mode = True
