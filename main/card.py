from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


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


engine = create_engine("sqlite:////tmp/index.db")
Base.metadata.create_all(engine)
