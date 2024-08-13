from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)

engine = create_engine("sqlite:////tmp/index.db")

Base = declarative_base()


class Card(Base):
    __tablename__ = "cards"
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    front_text = Column(String(255))
    back_text = Column(String(255))


# Create tables
Base.metadata.create_all(engine)


@app.post("/api/cards")
def card_post():
    front_text = request.form["frontText"]
    back_text = request.form["backText"]

    card = Card(front_text=front_text, back_text=back_text)

    # Create session
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    session.add(card)
    session.query(Card).order_by(Card.card_id.desc()).first()
    session.commit()

    return "OK"


def get_app():
    return app
