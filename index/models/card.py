from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import declarative_base

from index.database import get_engine


Base = declarative_base()


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    front_text = Column(String(255))
    back_text = Column(String(255))

    @property
    def frontText(self):
        return self.front_text

    @property
    def backText(self):
        return self.back_text


engine = get_engine()
Base.metadata.create_all(engine)