from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


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


class CardSchema(SQLAlchemySchema):
    class Meta:
        model = Card
        load_instance = True

    card_id = auto_field()
    front_text = auto_field()
    back_text = auto_field()


@app.post("/api/cards")
def card_post():
    front_text = request.form["frontText"]
    back_text = request.form["backText"]

    card = Card(front_text=front_text, back_text=back_text)

    # Create session
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    session.add(card)
    card_saved = session.query(Card).order_by(Card.card_id.desc()).first()
    session.commit()

    card_schema = CardSchema()
    json = card_schema.dump(card_saved)

    return json


def get_app():
    return app
