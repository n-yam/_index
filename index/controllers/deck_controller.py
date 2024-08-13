from flask import Blueprint, request

from index.models.card import Card
from index.models.card_schema import CardSchema
from index.database import get_session

deck_controller = Blueprint("deck_controller", __name__)


@deck_controller.post("/api/cards")
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
