from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from db import SessionLocal
from db import entries as db_entries
from .schemas import Entry, CreateEntry


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/browse/{entry_id}", response_model=Entry)
def get_entry(entry_id: int, db: Session = Depends(get_db)):
    return db_entries.get_single_entry(db, entry_id=entry_id)


@router.post("/browse/", response_model=Entry)
def create_entry(entry: CreateEntry, db: Session = Depends(get_db)):
    entries = db_entries.create_entry(db, entry)
    return entries


@router.get("/browse/", response_model=List[Entry])
def get_entries(db: Session = Depends(get_db)):
    entries = db_entries.get_entries(db)
    return entries
