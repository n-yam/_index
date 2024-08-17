import os
from uuid import uuid4
from sqlalchemy import func
from datetime import datetime

from index import config
from index.models.model import Card, Image, FrontImage, BackImage
from index.database import get_session
from index.config import CARD_LENGTH_MAX, IMAGE_DIR


class CardService:
    def add(self, card, files):
        try:
            for file in files.getlist("frontImage"):
                uuid = self.write_image_file(file)
                FrontImage(uuid=uuid, card=card)

            for file in files.getlist("backImage"):
                uuid = self.write_image_file(file)
                BackImage(uuid=uuid, card=card)

            with get_session() as session:
                session.add(card)
                session.commit()
                card_saved = session.query(Card).order_by(Card.id.desc()).first()
                return card_saved

        except Exception as e:
            raise e

    def write_image_file(self, file):
        uuid = uuid = str(uuid4())
        path = "{}/{}.jpg".format(config.IMAGE_DIR, uuid)
        file.save(path)

        return uuid

    def update(self, newCard, files):
        try:
            with get_session() as session:
                card = session.query(Card).filter_by(id=newCard.id).first()

                if card is None:
                    raise CardNotFoundException

                # Delete old data
                session.query(Image).filter_by(card_id=card.id).delete()
                self.remove_image_file(card)

                # Add new images
                for file in files.getlist("frontImage"):
                    uuid = self.write_image_file(file)
                    front_image = FrontImage(uuid=uuid, card=card)
                    session.add(front_image)

                for file in files.getlist("backImage"):
                    uuid = self.write_image_file(file)
                    back_image = BackImage(uuid=uuid, card=card)
                    session.add(back_image)

                # Update texts and etc.
                card.front_text = newCard.front_text
                card.back_text = newCard.back_text
                card.updated = datetime.now()

                session.commit()

                # Return
                card_updated = session.query(Card).filter_by(id=newCard.id).first()

                return card_updated

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

                if card is None:
                    raise CardNotFoundException

                return card

        except Exception as e:
            raise e

    def get_random(self):
        try:
            with get_session() as session:
                card = session.query(Card).order_by(func.random()).first()

                if card is None:
                    raise CardNotFoundException

                return card

        except Exception as e:
            raise e

    def remove(self, id):
        try:
            with get_session() as session:
                query = session.query(Card).filter(Card.id == id)
                card = query.first()

                if card is None:
                    raise CardNotFoundException

                query.delete()
                self.remove_image_file(card)

                session.commit()

        except Exception as e:
            raise e

    def remove_image_file(self, card):
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
