from db import Base
import enum
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Date, Text, Enum
from sqlalchemy.orm import relationship

entry_director_association = Table('entries_directors_m2m', Base.metadata,
                                   Column('entry_id', Integer, ForeignKey('entries.id')),
                                   Column('director_id', Integer, ForeignKey('directors.id'))
                                   )
entry_actor_association = Table('entries_actors_m2m', Base.metadata,
                                Column('entry_id', Integer, ForeignKey('entries.id')),
                                Column('actor_id', Integer, ForeignKey('actors.id'))
                                )
entry_country_association = Table('entries_countries_m2m', Base.metadata,
                                  Column('entry_id', Integer, ForeignKey('entries.id')),
                                  Column('country_id', Integer, ForeignKey('countries.id'))
                                  )
entry_genre_association = Table('entries_genres_m2m', Base.metadata,
                                Column('entry_id', Integer, ForeignKey('entries.id')),
                                Column('genre_id', Integer, ForeignKey('genres.id'))
                                )


class EntryType(str, enum.Enum):
    MOVIE = "Movie"
    TV_SHOW = "TV Show"


class EntryRating(str, enum.Enum):
    R = "R"
    NR = "NR"
    PG_13 = "PG-13"
    TV_PG = "TV-PG"
    TV_MA = "TV-MA"
    TV_14 = "TV-14"
    TV_Y7 = "TV-Y7"
    TV_Y7_FV = "TV-Y7-FV"


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    show_id = Column(String, unique=True)
    type = Column(Enum(EntryType), nullable=False)
    title = Column(String, nullable=False)
    directors = relationship("Director", secondary=entry_director_association, back_populates="shows")
    casts = relationship("Actor", secondary=entry_actor_association, back_populates="shows")
    countries = relationship("Country", secondary=entry_country_association, back_populates="shows")
    date_added = Column(Date, nullable=False)
    release_year = Column(String, nullable=False)
    rating = Column(Enum(EntryRating), default=EntryRating.NR)
    duration = Column(String, nullable=False)
    listed_in = relationship("Genre", secondary=entry_country_association, back_populates="shows")
    description = Column(Text, default="N/A")


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shows = relationship("Entry", back_populates="directors")


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shows = relationship("Entry", back_populates="actors")


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shows = relationship("Entry", back_populates="countries")


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
