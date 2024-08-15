from pytest import fixture

from index.wsgi import app

client = app.test_client()


@fixture
def auto_clean_up():
    clean_up()
    yield
    clean_up()


def test_count_empty(auto_clean_up):
    url = "/api/questions/count"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["total"] == 0
    assert response.json["fresh"] == 0
    assert response.json["finished"] == 0


def test_count_present(auto_clean_up):
    # Post
    card_post("FRONT_TEXT", "BACK_TEXT")

    url = "/api/questions/count"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["total"] == 1
    assert response.json["fresh"] == 1
    assert response.json["finished"] == 0


def clean_up():
    all_cards = card_get_all().json

    for card in all_cards:
        card_delete(card["id"])


def card_post(front_text, back_text):
    url = "/api/cards"
    formData = {
        "frontText": front_text,
        "backText": back_text,
    }
    response = client.post(url, data=formData)

    return response


def card_get(id):
    url = "/api/cards/{}".format(id)
    response = client.get(url)
    return response


def card_get_all():
    url = "/api/cards"
    response = client.get(url)
    return response


def card_delete(id):
    url = "/api/cards/{}".format(id)
    response = client.delete(url)
    return response
