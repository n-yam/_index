from index.models.card import Card
from index.database import get_session


class QuestionService:
    def count(self):
        try:
            with get_session() as session:
                total_count = session.query(Card).count()
                fresh_count = session.query(Card).filter(Card.fresh, True).count()
                finished_count = session.query(Card).filter(Card.finished, True).count()

                count = {
                    "total": total_count,
                    "fresh": fresh_count,
                    "finished": finished_count,
                }
                return count

        except Exception as e:
            raise e
