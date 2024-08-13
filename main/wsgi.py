from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main.card import Card

from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

app = Flask(__name__)
engine = create_engine("sqlite:////tmp/index.db")
Base = declarative_base()


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
