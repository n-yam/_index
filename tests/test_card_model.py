from datetime import datetime, timedelta

from index import config
from index.models.model import Card


def test_default_values():
    card = Card()

    assert card.level == 0
    assert card.next.strftime(config.DATE_FORMAT) == config.CARD_NEXT_DEFAULT
    assert card.updated is None
    assert card.todo is False
    assert card.done is False
    assert card.fresh is True


def test_level_up_from_min():
    card = Card()
    card.level_up()

    today = datetime.now().date()
    tomorrow = today + timedelta(days=config.CARD_LEVEL_ONE_INTERVAL)

    assert card.level == 1
    assert card.next == tomorrow
    assert card.updated.date() == today
    assert card.todo is False
    assert card.done is True
    assert card.fresh is True


def test_level_up_from_max():
    card = Card()
    card.level = config.CARD_LEVEL_MAX
    card.level_up()

    today = datetime.now().date()
    next = today + timedelta(days=config.CARD_LEVEL_NINE_INTERVAL)

    assert card.level == config.CARD_LEVEL_MAX
    assert card.next == next
    assert card.updated.date() == today
    assert card.todo is False
    assert card.done is True
    assert card.fresh is True


def test_level_down_from_min():
    card = Card()
    card.level_down()

    today = datetime.now().date()

    assert card.level == config.CARD_LEVEL_MIN
    assert card.next == today
    assert card.updated.date() == today
    assert card.todo is False
    assert card.done is False
    assert card.fresh is True


def test_level_down_from_max():
    card = Card()
    card.level = config.CARD_LEVEL_MAX
    card.level_down()

    today = datetime.now().date()
    next = today + timedelta(days=config.CARD_LEVEL_EIGHT_INTERVAL)

    assert card.level == config.CARD_LEVEL_MAX - 1
    assert card.next == next
    assert card.updated.date() == today
    assert card.todo is False
    assert card.done is True
    assert card.fresh is True
