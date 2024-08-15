from pytest import fixture
from datetime import datetime

from index.models.card import Card
from index.services.card_service import CardService
from index.services.question_service import QuestionService

card_service = CardService()
question_service = QuestionService()


@fixture
def auto_clean_up():
    clean_up()
    yield
    clean_up()


def test_reset(auto_clean_up):
    # Add
    card_service.add(Card())

    count = question_service.count()

    assert count["fresh"] == 1
    assert count["todo"] == 0
    assert count["done"] == 0

    # Reset
    now = datetime.now()
    question_service.reset(now)

    count_reset = question_service.count()

    assert count_reset["fresh"] == 1
    assert count_reset["todo"] == 1
    assert count_reset["done"] == 0


def clean_up():
    for card in card_service.get_all():
        card_service.remove(card.id)
