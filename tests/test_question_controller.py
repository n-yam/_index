from pytest import fixture

from index.wsgi import application
from tests import utils

client = application.test_client()


@fixture
def auto_cleanup():
    utils.cleanup()
    yield
    utils.cleanup()


def test_count_empty(auto_cleanup):
    url = "/api/questions/count"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["fresh"] == 0
    assert response.json["todo"] == 0
    assert response.json["done"] == 0


def test_count_present(auto_cleanup):
    # Post
    utils.card_post("FRONT_TEXT", "BACK_TEXT")

    url = "/api/questions/count"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["fresh"] == 1
    assert response.json["todo"] == 0
    assert response.json["done"] == 0


def test_reset(auto_cleanup):
    # Post
    utils.card_post("FRONT_TEXT", "BACK_TEXT")

    # Reset
    client.post("/api/questions/reset")

    # Count
    url = "/api/questions/count"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["fresh"] == 1
    assert response.json["todo"] == 1
    assert response.json["done"] == 0
