from index.wsgi import application

client = application.test_client()


def cleanup():
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


def card_post_with_images(front_text, back_text, front_images, back_images):
    url = "/api/cards"
    formData = {
        "frontText": front_text,
        "backText": back_text,
        "frontImage": front_images,
        "backImage": back_images,
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
