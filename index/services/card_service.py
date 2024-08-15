from datetime import datetime

from index.models.card import Card
from index.database import get_session
from index import config


class CardService:
    def add(self, card):
        try:
            card.created = datetime.now()

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
                    session.query(Card)
                    .order_by(Card.id.desc())
                    .limit(config.CARD_MAX_LENGTH)
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
                rows_count = session.query(Card).filter(Card.id == id).delete()
                session.commit()
                return rows_count

        except Exception as e:
            raise e
