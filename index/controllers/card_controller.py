from flask import Blueprint, request

from index.models.card import Card
from index.models.card_schema import CardSchema
from index.services.card_service import CardService

card_controller = Blueprint("card_controller", __name__)
card_service = CardService()


@card_controller.post("/api/cards")
def card_post():
    front_text = request.form["frontText"]
    back_text = request.form["backText"]

    card = Card(front_text=front_text, back_text=back_text)
    card_saved = card_service.add(card)

    json = CardSchema().dump(card_saved)

    return json


@card_controller.get("/api/cards")
def card_get_all():

    cards = card_service.get_all()
    json = CardSchema(many=True).dump(cards)

    return json


@card_controller.get("/api/cards/<id>")
def card_get(id):

    card = card_service.get(id)
    json = CardSchema().dump(card)

    return json
