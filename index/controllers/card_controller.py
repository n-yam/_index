from uuid import uuid4
from flask import Blueprint, request

from index import config
from index.models.model import Card, Image
from index.models.schema import CardSchema
from index.services.card_service import CardService

card_controller = Blueprint("card_controller", __name__)
card_service = CardService()


@card_controller.post("/api/cards")
def card_post():
    front_text = request.form["frontText"]
    back_text = request.form["backText"]

    card = Card(front_text=front_text, back_text=back_text)

    for file in request.files.getlist("frontImage"):
        uuid = uuid = str(uuid4())

        # Write to file
        path = "{}/{}.jpg".format(config.IMAGE_DIR, uuid)
        file.save(path)

        # Link to card
        Image(uuid=uuid, card=card)

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

    if card is None:
        return "", 404

    json = CardSchema().dump(card)

    return json


@card_controller.put("/api/cards/<id>")
def card_put(id):
    front_text = request.form["frontText"]
    back_text = request.form["backText"]

    card = Card(id=id, front_text=front_text, back_text=back_text)
    card_updated = card_service.update(card)

    if card_updated:
        json = CardSchema().dump(card_updated)
        return json

    else:
        return "", 404


@card_controller.delete("/api/cards/<id>")
def card_delete(id):

    if card_service.remove(id) == 0:
        return "", 404
    else:
        return "", 200
