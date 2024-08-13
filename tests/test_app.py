from index import wsgi


app = wsgi.get_app()
client = app.test_client()


def test_card_post():
    url = "/api/cards"

    front_text = "THIS IS FRONT TEXT"
    back_text = "THIS IS BACK TEXT"

    formData = {
        "frontText": front_text,
        "backText": back_text,
    }

    response = client.post(url, data=formData)

    assert response.status_code == 200
    assert response.json["frontText"] == front_text
    assert response.json["backText"] == back_text
