from datetime import datetime

from flask import Blueprint

from index.models.schema import CardSchema
from index.services.question_service import QuestionService

question_controller = Blueprint("question_controller", __name__)
question_service = QuestionService()


@question_controller.get("/api/questions/count")
def question_count_get():
    count = question_service.count()
    return count


@question_controller.post("/api/questions/reset")
def question_reset_post():
    now = datetime.now()
    question_service.reset(now)
    return ""


@question_controller.get("/api/questions/first")
def question_first_get():
    question = question_service.first()

    if question is None:
        return "", 404

    return CardSchema().dump(question)
