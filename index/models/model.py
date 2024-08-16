from datetime import datetime, timedelta

from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Boolean

from index import config
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

    def level_up(self):
        if self.level < config.CARD_MAX_LEVEL:
            self.level += 1
            self.next = datetime.now() + self.calc_interval()
            self.done = True

        self.updated = datetime.now()

    def level_down(self):
        if config.CARD_MIN_LEVEL < self.level:
            self.level -= 1
            self.next = datetime.now() + self.calc_interval()
            self.done = True

        self.updated = datetime.now()

    def calc_interval(self):
        if self.level == 0:
            return timedelta(days=0)
        if self.level == 1:
            return timedelta(days=1)
        if self.level == 2:
            return timedelta(days=3)
        if self.level == 3:
            return timedelta(days=5)
        if self.level == 4:
            return timedelta(days=7)
        if self.level == 5:
            return timedelta(days=15)
        if self.level == 6:
            return timedelta(days=30)
        if self.level == 7:
            return timedelta(days=60)
        if self.level == 8:
            return timedelta(days=90)
        if self.level == 9:
            return timedelta(days=120)


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
