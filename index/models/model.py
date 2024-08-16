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
    front_images = relationship(
        "FrontImage",
        primaryjoin="and_(FrontImage.card_id == Card.id, FrontImage.side=='front')",
        back_populates="card",
        lazy="joined",
    )
    back_images = relationship(
        "BackImage",
        primaryjoin="and_(BackImage.card_id == Card.id, BackImage.side=='back')",
        back_populates="card",
        lazy="joined",
    )


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36))
    side = Column(String(5))
    card_id = mapped_column(ForeignKey("cards.id"))


class FrontImage(Image):

    def __init__(self, *args, **kwargs):
        super(FrontImage, self).__init__(*args, **kwargs)
        self.side = "front"

    card = relationship("Card", back_populates="front_images")


class BackImage(Image):

    def __init__(self, *args, **kwargs):
        super(BackImage, self).__init__(*args, **kwargs)
        self.side = "back"

    card = relationship("Card", back_populates="back_images")
