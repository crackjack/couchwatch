from sqlalchemy.orm import Session

from entries.models import Entry
from entries.schemas import Entry


def get_single_entry(db: Session, show_id: str):
    return db.query(Entry).filter(Entry.show_id == show_id).first()


def get_entries(db: Session):
    return db.query(Entry).all()


def create_entry(db: Session, entry: Entry):
    db_entry = Entry(
        show_id=entry.show_id,
        title=entry.title,
        directors=[director for director in entry.directors],
        casts=[cast for cast in entry.casts],
        countries=[country for country in entry.countries],
        type=entry.type,
        date_added=entry.date_added,
        release_year=entry.release_year,
        rating=entry.rating,
        duration=entry.duration,
        listed_in=[genre for genre in entry.genres],
        description=entry.description
    )

    # for director in entry.directors:
    #     try:
    #         db_entry.directors.append(
    #             Director(name=director.name)
    #         )
    #     except ValidationError:
    #         pass
    #
    # for cast in entry.casts:
    #     try:
    #         db_entry.casts.append(
    #             Actor(name=cast.name)
    #         )
    #     except ValidationError:
    #         pass
    #
    # for country in entry.countries:
    #     try:
    #         db_entry.countries.append(
    #             Country(name=country.name)
    #         )
    #     except ValidationError:
    #         pass
    #
    # for genre in entry.genres:
    #     try:
    #         db_entry.genres.append(
    #             Genre(name=genre.name)
    #         )
    #     except ValidationError:
    #         pass

    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete_entry(db: Session, show_id: str):
    return db.query(Entry).filter(Entry.show_id == show_id).delete(synchronize_session="fetch")
