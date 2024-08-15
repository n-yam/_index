from index.wsgi import app

client = app.test_client()


def test_card_post():
    front_text = "[POST] THIS IS FRONT TEXT"
    back_text = "[POST] THIS IS BACK TEXT"

    response = card_post(front_text, back_text)

    assert response.status_code == 200
    assert response.json["frontText"] == front_text
    assert response.json["backText"] == back_text


def test_card_get_all():
    # Post
    front_text = "[GET_ALL] THIS IS FRONT TEXT"
    back_text = "[GET_ALL] THIS IS BACK TEXT"
    card_post(front_text, back_text)

    # Get all
    url = "/api/cards"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json[0]["frontText"] == front_text
    assert response.json[0]["backText"] == back_text


def test_card_get():
    # Post
    front_text = "[GET] THIS IS FRONT TEXT"
    back_text = "[GET] THIS IS BACK TEXT"
    response = card_post(front_text, back_text)
    id = response.json["id"]

    # Get
    url = "/api/cards/{}".format(id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.json["frontText"] == front_text
    assert response.json["backText"] == back_text


def test_card_put():
    # Post
    front_text_before = "[POST] THIS IS FRONT TEXT"
    back_text_before = "[POST] THIS IS BACK TEXT"
    response = card_post(front_text_before, back_text_before)
    id = response.json["id"]

    # Put
    url = "/api/cards/{}".format(id)
    front_text_after = "[PUT] ## FRONT TEXT ##"
    back_text_after = "[PUT] ## BACK TEXT ##"

    formData = {
        "frontText": front_text_after,
        "backText": back_text_after,
    }

    response = client.put(url, data=formData)

    assert response.status_code == 200
    assert response.json["frontText"] == front_text_after
    assert response.json["backText"] == back_text_after


def card_post(front_text, back_text):
    url = "/api/cards"
    formData = {
        "frontText": front_text,
        "backText": back_text,
    }

    response = client.post(url, data=formData)

    return response
