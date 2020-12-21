from db import Base
import enum
from sqlalchemy import Column, Integer, String, \
    Table, ForeignKey, Date, Text, Enum
from sqlalchemy.orm import relationship

entry_director_association = Table('entries_directors_m2m', Base.metadata,
                                   Column('entry_id', Integer,
                                          ForeignKey('entries.id'),
                                          primary_key=True),
                                   Column('director_id', Integer,
                                          ForeignKey('directors.id'),
                                          primary_key=True)
                                   )
entry_actor_association = Table('entries_actors_m2m', Base.metadata,
                                Column('entry_id', Integer,
                                       ForeignKey('entries.id'),
                                       primary_key=True),
                                Column('actor_id', Integer,
                                       ForeignKey('actors.id'),
                                       primary_key=True)
                                )
entry_country_association = Table('entries_countries_m2m', Base.metadata,
                                  Column('entry_id', Integer,
                                         ForeignKey('entries.id'),
                                         primary_key=True),
                                  Column('country_id', Integer,
                                         ForeignKey('countries.id'),
                                         primary_key=True)
                                  )
entry_genre_association = Table('entries_genres_m2m', Base.metadata,
                                Column('entry_id', Integer,
                                       ForeignKey('entries.id'),
                                       primary_key=True),
                                Column('genre_id', Integer,
                                       ForeignKey('genres.id'),
                                       primary_key=True)
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


class EntryTable(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    show_id = Column(String, unique=True)
    type = Column(Enum(EntryType), nullable=False)
    title = Column(String, nullable=False)
    directors = relationship("DirectorTable",
                             secondary=entry_director_association)
    casts = relationship("ActorTable",
                         secondary=entry_actor_association)
    countries = relationship("CountryTable",
                             secondary=entry_country_association)
    date_added = Column(Date, nullable=False)
    release_year = Column(String, nullable=False)
    rating = Column(Enum(EntryRating), default=EntryRating.NR)
    duration = Column(String, nullable=False)
    listed_in = relationship("GenreTable", secondary=entry_genre_association)
    description = Column(Text, default="N/A")


class DirectorTable(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shows = relationship("EntryTable", secondary=entry_director_association)


class ActorTable(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shows = relationship("EntryTable", secondary=entry_actor_association)


class CountryTable(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shows = relationship("EntryTable", secondary=entry_country_association)


class GenreTable(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shows = relationship("EntryTable", secondary=entry_genre_association)
