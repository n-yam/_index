from index.models.card import Card
from index.database import get_session
from index import config


class CardService:
    def add(self, card):
        session = get_session()

        try:
            session.add(card)
            session.commit()
            card_saved = session.query(Card).order_by(Card.id.desc()).first()

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()

        return card_saved

    def get_all(self):
        session = get_session()

        try:
            cards = (
                session.query(Card)
                .order_by(Card.id.desc())
                .limit(config.CARD_MAX_LENGTH)
            )

        except Exception as e:
            raise e

        finally:
            session.close()

        return cards

    def get(self, id):
        session = get_session()

        try:
            card = session.get(Card, id)

        except Exception as e:
            raise e

        finally:
            session.close()

        return card
