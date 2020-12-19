from db import Base
from sqlalchemy import Column, Integer, String


class Entries(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
