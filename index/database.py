from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:////tmp/index.db")


def get_session():
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    return session


def get_engine():
    return engine
