from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

from index import config
from index.models.base import Base


def get_session():
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    return session


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


engine = create_engine(config.DATABASE_URL)
Base.metadata.create_all(engine)
