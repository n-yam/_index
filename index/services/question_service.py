from datetime import datetime

from index import config
from index.models.model import Card
from index.database import get_session


class QuestionService:
    def count(self):
        try:
            with get_session() as session:
                fresh_count = (
                    session.query(Card)
                    .filter((Card.fresh.is_(True)) & (Card.todo.is_(True)))
                    .count()
                )
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
                for question in (
                    session.query(Card)
                    .filter(Card.fresh.is_(True))
                    .order_by(Card.created.asc())
                    .limit(config.QUESTION_FRESH_MAX)
                ):
                    question.todo = True

                for question in session.query(Card).filter(
                    (Card.fresh.is_(False)) & (Card.next <= now)
                ):
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

                if question is None:
                    raise QuestionNotFoundException

                return question

        except Exception as e:
            raise e

    def answer(self, answer):
        try:
            card = self.first()

            if card is None:
                raise QuestionNotFoundException

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


class QuestionNotFoundException(Exception):
    def __init__(self, arg=""):
        self.arg = arg
