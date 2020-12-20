from pydantic import BaseModel
from typing import Optional


class BaseEntry(BaseModel):
    name: str
    netflix_id: Optional[str] = None


class Entry(BaseEntry):

    class Config:
        orm_mode = True
