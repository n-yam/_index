from pytest import fixture

from index.wsgi import app
from tests import utils

client = app.test_client()


@fixture
def auto_clean_up():
    utils.clean_up()
    yield
    utils.clean_up()


def test_count_empty(auto_clean_up):
    url = "/api/questions/count"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["total"] == 0
    assert response.json["fresh"] == 0
    assert response.json["finished"] == 0


def test_count_present(auto_clean_up):
    # Post
    utils.card_post("FRONT_TEXT", "BACK_TEXT")

    url = "/api/questions/count"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["total"] == 1
    assert response.json["fresh"] == 1
    assert response.json["finished"] == 0
