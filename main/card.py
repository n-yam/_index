from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class Card(Base):
    __tablename__ = "cards"
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    front_text = Column(String(255))
    back_text = Column(String(255))


engine = create_engine("sqlite:////tmp/index.db")
Base.metadata.create_all(engine)
