from flask import Blueprint, request

from index.models.card import Card
from index.models.card_schema import CardSchema
from index.services.deck_service import DeckService

deck_controller = Blueprint("deck_controller", __name__)
deck_service = DeckService()


@deck_controller.post("/api/cards")
def card_post():
    front_text = request.form["frontText"]
    back_text = request.form["backText"]

    card = Card(front_text=front_text, back_text=back_text)
    card_saved = deck_service.add(card)

    json = CardSchema().dump(card_saved)

    return json
