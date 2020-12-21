from sqlalchemy.orm import Session

from entries.models import Entry
from entries.schemas import EntryTable, DirectorTable, ActorTable, CountryTable, GenreTable


def get_single_entry(db: Session, show_id: str):
    return db.query(EntryTable).filter(EntryTable.show_id == show_id).first()


def get_entries(db: Session):
    return db.query(EntryTable).all()


def create_entry(db: Session, entry: Entry):
    db_entry = EntryTable(
        show_id=entry.show_id,
        title=entry.title,
        type=entry.type,
        date_added=entry.date_added,
        release_year=entry.release_year,
        rating=entry.rating,
        duration=entry.duration,
        description=entry.description
    )

    for director in entry.directors:
        name = director.name.strip()
        if not (name and director_exists(db, name)):
            db_entry.directors.append(DirectorTable(name=name))

    for cast in entry.casts:
        name = cast.name.strip()
        if not (name and cast_exists(db, name)):
            db_entry.casts.append(ActorTable(name=name))

    for country in entry.countries:
        name = country.name.strip()
        if not (name and country_exists(db, name)):
            db_entry.countries.append(CountryTable(name=name))

    for genre in entry.listed_in:
        name = genre.name.strip()
        if not (name and genre_exists(db, name)):
            db_entry.listed_in.append(GenreTable(name=name))

    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete_entry(db: Session, show_id: str):
    return db.query(EntryTable).filter(EntryTable.show_id == show_id).delete(synchronize_session="fetch")


def director_exists(db: Session, name: str):
    return False if not db.query(DirectorTable).filter(DirectorTable.name == name).first() else True


def cast_exists(db: Session, name: str):
    return False if not db.query(ActorTable).filter(ActorTable.name == name).first() else True


def country_exists(db: Session, name: str):
    return False if not db.query(CountryTable).filter(CountryTable.name == name).first() else True


def genre_exists(db: Session, name: str):
    return False if not db.query(GenreTable).filter(GenreTable.name == name).first() else True
