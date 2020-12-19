from sqlalchemy.orm import Session

from entries.models import Entries
from entries.schemas import CreateEntry


def get_single_entry(db: Session, entry_id: int):
    return db.query(Entries).filter(Entries.id == entry_id).first()


def get_entries(db: Session):
    return db.query(Entries).all()


def create_entry(db: Session, entry: CreateEntry):
    db_entry = Entries(name=entry.name, netflix_id=entry.netflix_id)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
