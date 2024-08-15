from index.models.card import Card
from index.database import get_session


class QuestionService:
    def count(self):
        try:
            with get_session() as session:
                total_count = session.query(Card).count()
                fresh_count = session.query(Card).filter(Card.fresh, True).count()
                done_count = session.query(Card).filter(Card.done, True).count()

                count = {
                    "total": total_count,
                    "fresh": fresh_count,
                    "done": done_count,
                }
                return count

        except Exception as e:
            raise e
