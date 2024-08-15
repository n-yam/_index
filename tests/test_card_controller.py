from pytest import fixture
from datetime import datetime

from index.wsgi import app
from index.config import DATETIME_FORMAT, CARD_NEXT_DEFAULT
from tests import utils

client = app.test_client()


@fixture
def auto_clean_up():
    clean_up()
    yield
    clean_up()


def test_card_post(auto_clean_up):
    front_text = "[POST] THIS IS FRONT TEXT"
    back_text = "[POST] THIS IS BACK TEXT"

    response = utils.card_post(front_text, back_text)

    assert response.status_code == 200
    assert response.json["frontText"] == front_text
    assert response.json["backText"] == back_text
    assert response.json["level"] == 0
    assert response.json["fresh"] is True
    assert response.json["finished"] is False
    assert response.json["next"] == CARD_NEXT_DEFAULT
    assert response.json["created"] == datetime.now().strftime(DATETIME_FORMAT)
    assert response.json["updated"] is None


def test_card_get_all(auto_clean_up):
    # Post
    front_text = "[GET_ALL] THIS IS FRONT TEXT"
    back_text = "[GET_ALL] THIS IS BACK TEXT"
    response_post = utils.card_post(front_text, back_text)
    assert response_post.status_code == 200

    # Get all
    response_get = utils.card_get_all()

    assert response_get.status_code == 200
    assert response_get.json[0]["frontText"] == front_text
    assert response_get.json[0]["backText"] == back_text
    assert response_get.json[0]["level"] == 0
    assert response_get.json[0]["fresh"] is True
    assert response_get.json[0]["finished"] is False
    assert response_get.json[0]["next"] == CARD_NEXT_DEFAULT
    assert response_get.json[0]["created"] == datetime.now().strftime(DATETIME_FORMAT)
    assert response_get.json[0]["updated"] is None


def test_card_get(auto_clean_up):
    # Post
    front_text = "[GET] THIS IS FRONT TEXT"
    back_text = "[GET] THIS IS BACK TEXT"
    response_post = utils.card_post(front_text, back_text)
    assert response_post.status_code == 200

    id = response_post.json["id"]

    # Get
    response_get = utils.card_get(id)

    assert response_get.status_code == 200
    assert response_get.json["frontText"] == front_text
    assert response_get.json["backText"] == back_text
    assert response_get.json["level"] == 0
    assert response_get.json["fresh"] is True
    assert response_get.json["finished"] is False
    assert response_get.json["next"] == CARD_NEXT_DEFAULT
    assert response_get.json["created"] == datetime.now().strftime(DATETIME_FORMAT)
    assert response_get.json["updated"] is None


def test_card_get_404(auto_clean_up):
    unknown_id = 99999
    response_get = utils.card_get(unknown_id)

    assert response_get.status_code == 404
    assert response_get.json is None


def test_card_put(auto_clean_up):
    # Post
    front_text_before = "[POST] THIS IS FRONT TEXT"
    back_text_before = "[POST] THIS IS BACK TEXT"
    response_post = utils.card_post(front_text_before, back_text_before)
    assert response_post.status_code == 200

    id = response_post.json["id"]

    # Put
    url = "/api/cards/{}".format(id)
    front_text_after = "[PUT] ## FRONT TEXT ##"
    back_text_after = "[PUT] ## BACK TEXT ##"

    formData = {
        "frontText": front_text_after,
        "backText": back_text_after,
    }

    response_put = client.put(url, data=formData)

    assert response_put.status_code == 200
    assert response_put.json["frontText"] == front_text_after
    assert response_put.json["backText"] == back_text_after
    assert response_put.json["level"] == 0
    assert response_put.json["fresh"] is True
    assert response_put.json["finished"] is False
    assert response_put.json["next"] == CARD_NEXT_DEFAULT
    assert response_put.json["created"] == datetime.now().strftime(DATETIME_FORMAT)
    assert response_put.json["updated"] == datetime.now().strftime(DATETIME_FORMAT)


def test_card_put_404(auto_clean_up):
    unknown_id = 99999
    url = "/api/cards/{}".format(unknown_id)
    formData = {
        "frontText": "",
        "backText": "",
    }

    response = client.put(url, data=formData)

    assert response.status_code == 404
    assert response.json is None


def test_card_delete(auto_clean_up):
    # Post
    response_post = utils.card_post("FRONT_TEXT", "BACK_TEXT")
    assert response_post.status_code == 200

    id = response_post.json["id"]

    # Delete
    response_delete = utils.card_delete(id)
    assert response_delete.status_code == 200

    # Get
    response_get = utils.card_get(id)
    assert response_get.status_code == 404


def test_card_delete404(auto_clean_up):
    unknown_id = 99999
    response = utils.card_delete(unknown_id)

    assert response.status_code == 404
    assert response.json is None


def clean_up():
    all_cards = utils.card_get_all().json

    for card in all_cards:
        utils.card_delete(card["id"])
