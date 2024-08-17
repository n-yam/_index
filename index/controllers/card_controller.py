from flask import Blueprint, request

from index.models.model import Card
from index.models.schema import CardSchema
from index.services.card_service import CardService, CardNotFoundException

card_controller = Blueprint("card_controller", __name__)
card_service = CardService()


@card_controller.post("/api/cards")
def card_post():
    try:
        front_text = request.form["frontText"]
        back_text = request.form["backText"]

        card = Card(front_text=front_text, back_text=back_text)
        files = request.files

        card_saved = card_service.add(card, files)
        json = CardSchema().dump(card_saved)

        return json

    except Exception as e:
        print(e)
        return "", 500


@card_controller.get("/api/cards")
def card_get_all():
    try:
        cards = card_service.get_all()
        json = CardSchema(many=True).dump(cards)
        return json

    except Exception as e:
        print(e)
        return "", 500


@card_controller.get("/api/cards/<id>")
def card_get(id):
    try:
        card = card_service.get(id)
        json = CardSchema().dump(card)
        return json

    except CardNotFoundException:
        return "", 404

    except Exception as e:
        print(e)
        return "", 500


@card_controller.get("/api/cards/random")
def card_get_random():
    try:
        card = card_service.get_random()
        json = CardSchema().dump(card)
        return json

    except CardNotFoundException:
        return "", 404

    except Exception as e:
        print(e)
        return "", 500


@card_controller.put("/api/cards/<id>")
def card_put(id):
    try:
        front_text = request.form["frontText"]
        back_text = request.form["backText"]

        card = Card(id=id, front_text=front_text, back_text=back_text)

        card_updated = card_service.update(card)
        json = CardSchema().dump(card_updated)

        return json

    except CardNotFoundException:
        return "", 404

    except Exception as e:
        print(e)
        return "", 500


@card_controller.delete("/api/cards/<id>")
def card_delete(id):
    try:
        card_service.remove(id)
        return "", 200

    except CardNotFoundException:
        return "", 404

    except Exception as e:
        print(e)
        return "", 500
