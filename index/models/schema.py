from marshmallow import Schema, fields

from index.config import DATETIME_FORMAT


class CamelCaseSchema(Schema):
    # https://marshmallow.readthedocs.io/en/latest/examples.html#inflection-camel-casing-keys
    def camelcase(self, s):
        parts = iter(s.split("_"))
        return next(parts) + "".join(i.title() for i in parts)

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = self.camelcase(field_obj.data_key or field_name)


class ImageSchema(CamelCaseSchema):
    id = fields.Int()
    uuid = fields.Str()


class CardSchema(CamelCaseSchema):
    id = fields.Int()
    front_text = fields.Str(required=True)
    back_text = fields.Str(required=True)
    front_images = fields.Nested(ImageSchema, many=True)
    level = fields.Integer()
    fresh = fields.Bool()
    todo = fields.Bool()
    done = fields.Bool()
    next = fields.DateTime(format=DATETIME_FORMAT)
    created = fields.DateTime(format=DATETIME_FORMAT)
    updated = fields.DateTime(format=DATETIME_FORMAT)
