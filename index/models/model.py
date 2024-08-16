from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Boolean

from index.models.base import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    front_text = Column(String(255))
    back_text = Column(String(255))
    level = Column(Integer)
    fresh = Column(Boolean)
    todo = Column(Boolean)
    done = Column(Boolean)
    next = Column(DateTime)
    created = Column(DateTime)
    updated = Column(DateTime)
    front_images = relationship("Image", back_populates="card", lazy="joined")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36))
    card_id = mapped_column(ForeignKey("cards.id"))
    card = relationship("Card", back_populates="front_images")
