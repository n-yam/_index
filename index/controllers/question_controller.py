from datetime import datetime

from flask import Blueprint, request

from index.models.schema import CardSchema
from index.services.question_service import QuestionService, QuestionNotFoundException

question_controller = Blueprint("question_controller", __name__)
question_service = QuestionService()


@question_controller.get("/api/questions/count")
def question_count_get():
    try:
        count = question_service.count()
        return count

    except Exception as e:
        print(e)
        return "", 500


@question_controller.post("/api/questions/reset")
def question_reset_post():
    try:
        now = datetime.now()
        question_service.reset(now)
        return ""

    except Exception as e:
        print(e)
        return "", 500


@question_controller.get("/api/questions/first")
def question_first_get():
    try:
        question = question_service.first()
        json = CardSchema().dump(question)

        return json

    except QuestionNotFoundException:
        return "", 404

    except Exception as e:
        print(e)
        return "", 500


@question_controller.post("/api/questions/first")
def question_answer_post():
    try:
        answer = request.args.get("answer")
        card_updated = question_service.answer(answer)
        json = CardSchema().dump(card_updated)

        return json

    except QuestionNotFoundException:
        return "", 404

    except Exception as e:
        print(e)
        return "", 500
