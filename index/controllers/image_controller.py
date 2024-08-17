from flask import Blueprint, send_file

from index import config

image_controller = Blueprint("image_controller", __name__)


@image_controller.get("/images/<uuid>")
def images_get(uuid):
    try:
        path = "{}/{}.jpg".format(config.IMAGE_DIR, uuid)
        response = send_file(path, mimetype="image/jpeg")

        return response

    except FileNotFoundError:
        return "", 404
