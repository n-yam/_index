from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime

from index.models.base import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    front_text = Column(String(255))
    back_text = Column(String(255))
    created = Column(DateTime)
    updated = Column(DateTime)
