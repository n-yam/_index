from flask import Blueprint, send_file

from index import config

image_controller = Blueprint("image_controller", __name__)


@image_controller.get("/images/<uuid>")
def images_get(uuid):
    path = "{}/{}.jpg".format(config.IMAGE_DIR, uuid)

    return send_file(path, mimetype="image/jpeg")
