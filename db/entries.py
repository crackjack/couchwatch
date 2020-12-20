from sqlalchemy.orm import Session

from entries.models import Entries
from entries.schemas import Entry


def get_single_entry(db: Session, netflix_id: str):
    return db.query(Entries).filter(Entries.netflix_id == netflix_id).first()


def get_entries(db: Session):
    return db.query(Entries).all()


def create_entry(db: Session, entry: Entry):
    db_entry = Entries(name=entry.name, netflix_id=entry.netflix_id)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete_entry(db: Session, netflix_id: str):
    return db.query(Entries).filter(Entries.netflix_id == netflix_id).delete(synchronize_session="fetch")
