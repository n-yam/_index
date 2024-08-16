import os
from datetime import datetime

from index.models.model import Card, Image
from index.database import get_session
from index.config import CARD_LENGTH_MAX, IMAGE_DIR


class CardService:
    def add(self, card):
        try:
            with get_session() as session:
                session.add(card)
                session.commit()
                card_saved = session.query(Card).order_by(Card.id.desc()).first()
                return card_saved

        except Exception as e:
            raise e

    def update(self, newCard):
        try:
            with get_session() as session:
                card = session.query(Card).filter_by(id=newCard.id).first()
                if card:
                    card.front_text = newCard.front_text
                    card.back_text = newCard.back_text
                    card.updated = datetime.now()
                    session.commit()
                    card_updated = session.query(Card).filter_by(id=newCard.id).first()
                    return card_updated
                else:
                    return None

        except Exception as e:
            raise e

    def get_all(self):
        try:
            with get_session() as session:
                cards = (
                    session.query(Card).order_by(Card.id.desc()).limit(CARD_LENGTH_MAX)
                )

                return cards

        except Exception as e:
            raise e

    def get(self, id):
        try:
            with get_session() as session:
                card = session.get(Card, id)
                return card

        except Exception as e:
            raise e

    def remove(self, id):
        try:
            with get_session() as session:
                card = session.query(Card).filter(Card.id == id).first()
                if card is None:
                    raise CardNotFoundException
                self.remove_image(card)

            with get_session() as session:
                session.query(Card).filter(Card.id == id).delete()
                session.query(Image).filter(Image.card_id == id).delete()
                session.commit()

        except Exception as e:
            raise e

    def remove_image(self, card):
        images = []

        for front_image in card.front_images:
            images.append(front_image)

        for back_image in card.back_images:
            images.append(back_image)

        for image in images:
            path = "{}/{}.jpg".format(IMAGE_DIR, image.uuid)
            os.remove(path)


class CardNotFoundException(Exception):
    def __init__(self, arg=""):
        self.arg = arg
