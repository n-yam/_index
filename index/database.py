from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from index import config
from index.models.base import Base

engine = create_engine(config.DATABASE_URL)
Base.metadata.create_all(engine)  # Create tables


def get_session():
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    return session
