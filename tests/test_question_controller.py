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


def test_first(auto_cleanup):
    # Post
    front_text = "FRONT_TEXT"
    back_text = "BACK_TEXT"
    utils.card_post(front_text, back_text)

    # Reset
    client.post("/api/questions/reset")

    # First
    response = client.get("/api/questions/first")

    assert response.status_code == 200
    assert response.json["frontText"] == front_text
    assert response.json["backText"] == back_text


def test_answer_one(auto_cleanup):
    # Post
    utils.card_post("", "")

    # Reset
    client.post("/api/questions/reset")

    # Answer
    response_answer = client.post("/api/questions/first?answer=1")

    assert response_answer.status_code == 200
    assert response_answer.json["done"] is True

    # Count
    response_count = client.get("/api/questions/count")

    assert response_count.json["fresh"] == 1
    assert response_count.json["todo"] == 1
    assert response_count.json["done"] == 1

    # First
    response_question = client.post("/api/questions/first")

    assert response_question.status_code == 404


def test_answer_zero(auto_cleanup):
    # Post
    utils.card_post("", "")

    # Reset
    client.post("/api/questions/reset")

    # Answer
    response_answer = client.post("/api/questions/first?answer=0")

    assert response_answer.status_code == 200
    assert response_answer.json["done"] is False

    # Count
    response_count = client.get("/api/questions/count")

    assert response_count.json["fresh"] == 1
    assert response_count.json["todo"] == 1
    assert response_count.json["done"] == 0

    # First
    response_question = client.post("/api/questions/first")

    assert response_question.status_code == 200


def test_answer_rotate(auto_cleanup):
    # Post
    utils.card_post("", "")
    utils.card_post("", "")
    utils.card_post("", "")

    # Reset
    client.post("/api/questions/reset")

    # Rotate
    assert client.post("/api/questions/first").json["id"] == 1

    client.post("/api/questions/first?answer=0")
    assert client.post("/api/questions/first").json["id"] == 2

    client.post("/api/questions/first?answer=0")
    assert client.post("/api/questions/first").json["id"] == 3

    client.post("/api/questions/first?answer=0")
    assert client.post("/api/questions/first").json["id"] == 1

    client.post("/api/questions/first?answer=0")
    assert client.post("/api/questions/first").json["id"] == 2

    client.post("/api/questions/first?answer=0")
    assert client.post("/api/questions/first").json["id"] == 3
