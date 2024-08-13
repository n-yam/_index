from main import wsgi


app = wsgi.get_app()
client = app.test_client()


def test_card_post():
    url = "/api/cards"

    frontText = "THIS IS FRONT TEXT"
    backText = "THIS IS BACK TEXT"

    formData = {
        "frontText": frontText,
        "backText": backText,
    }

    response = client.post(url, data=formData)

    assert response.status_code == 200
    assert response.json["frontText"] == frontText
    assert response.json["backText"] == backText
