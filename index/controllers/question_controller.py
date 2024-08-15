from flask import Blueprint

from index.services.question_service import QuestionService

question_controller = Blueprint("question_controller", __name__)
question_service = QuestionService()


@question_controller.get("/api/questions/count")
def question_count_get():
    count = question_service.count()
    return count
