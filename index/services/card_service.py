from index.models.card import Card
from index.database import get_session


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
