from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime, date
from .schemas import EntryType, EntryRating


class Director(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Actor(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Country(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Genre(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Entry(BaseModel):
    show_id: str
    title: str
    type: EntryType = Field(..., title="Type of Entry")
    directors: Optional[List[Director]] = []
    casts: Optional[List[Actor]] = []
    countries: Optional[List[Country]] = []
    date_added: date
    release_year: str
    rating: EntryRating = Field(..., title="Viewer Rating")
    duration: str
    listed_in: Optional[List[Genre]] = []
    description: Optional[str]

    class Config:
        orm_mode = True
