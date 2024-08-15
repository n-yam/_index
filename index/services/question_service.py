from index.models.card import Card
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
