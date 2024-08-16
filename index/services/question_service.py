from datetime import datetime

from index.models.model import Card
from index.database import get_session


class QuestionService:
    def count(self):
        try:
            with get_session() as session:
                fresh_count = session.query(Card).filter(Card.fresh, True).count()
                todo_count = session.query(Card).filter(Card.todo, True).count()
                done_count = session.query(Card).filter(Card.done, True).count()

                count = {
                    "fresh": fresh_count,
                    "todo": todo_count,
                    "done": done_count,
                }
                return count

        except Exception as e:
            raise e

    def reset(self, now):
        try:
            with get_session() as session:
                # Clear
                for question in session.query(Card).all():
                    question.todo = False

                # Setup
                for question in session.query(Card).filter(Card.next <= now):
                    question.todo = True

                session.commit()

        except Exception as e:
            raise e

    def first(self):
        try:
            with get_session() as session:
                question = (
                    session.query(Card)
                    .filter((Card.todo.is_(True)) & (Card.next < datetime.now()))
                    .order_by(Card.updated.asc())
                    .first()
                )

                return question

        except Exception as e:
            raise e

    def answer(self, answer):
        try:
            card = self.first()

            if answer == "0":
                card.level_down()

            elif answer == "1":
                card.level_up()

            with get_session() as session:
                session.add(card)
                session.commit()
                card_updated = session.query(Card).filter_by(id=card.id).first()
                return card_updated

        except Exception as e:
            raise e
