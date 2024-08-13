from flask import Flask, request
from sqlalchemy.orm import declarative_base

from index.card import Card
from index.card_schema import CardSchema
from index.database import get_session

app = Flask(__name__)
Base = declarative_base()


@app.post("/api/cards")
def card_post():
    front_text = request.form["frontText"]
    back_text = request.form["backText"]

    card = Card(front_text=front_text, back_text=back_text)

    session = get_session()
    session.add(card)
    card_saved = session.query(Card).order_by(Card.id.desc()).first()
    session.commit()

    card_schema = CardSchema()
    json = card_schema.dump(card_saved)

    return json


def get_app():
    return app
