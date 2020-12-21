from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session

from db import get_db, entries as db_entries
from .models import Entry


router = APIRouter()


@router.get("/browse/{show_id}", response_model=Entry, responses={
    404: {"detail": "Entry not found."}
})
def get_entry(show_id: str, db: Session = Depends(get_db)):
    entry = db_entries.get_single_entry(db, show_id=show_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found.")
    return entry


@router.post("/browse/", status_code=status.HTTP_201_CREATED, response_model=Entry, responses={
    400: {"detail": "Something bad happened."}
})
def create_entry(entry: Entry, db: Session = Depends(get_db)):
    entry = db_entries.create_entry(db, entry)
    if not entry:
        raise HTTPException(status_code=400, detail="Something bad happened.")
    return entry


@router.get("/browse/", response_model=List[Entry])
def get_entries(db: Session = Depends(get_db)):
    entries = db_entries.get_entries(db)
    return entries


@router.delete("/browse/{show_id}", response_class=Response, responses={
    200: {"detail": "Successfully Deleted"},
    404: {"detail": "Entry not found."}
})
def delete_entry(show_id: str, db: Session = Depends(get_db)):
    return Response(status_code=200) if db_entries.delete_entry(db, show_id=show_id) else Response(status_code=404)

