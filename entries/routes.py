from fastapi import APIRouter, Depends, HTTPException, status
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


@router.get("/browse/{entry_id}", status_code=status.HTTP_200_OK, response_model=Entry)
def get_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db_entries.get_single_entry(db, entry_id=entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not Found")
    return {"entry": entry}


@router.post("/browse/", status_code=status.HTTP_201_CREATED, response_model=Entry)
def create_entry(entry: CreateEntry, db: Session = Depends(get_db)):
    entries = db_entries.create_entry(db, entry)
    return entries


@router.get("/browse/", status_code=status.HTTP_200_OK, response_model=List[Entry])
def get_entries(db: Session = Depends(get_db)):
    entries = db_entries.get_entries(db)
    return entries
