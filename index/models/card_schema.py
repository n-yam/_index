from marshmallow import fields

from index.config import DATETIME_FORMAT
from index.models.camel_case_schema import CamelCaseSchema


class CardSchema(CamelCaseSchema):
    id = fields.Int()
    front_text = fields.Str(required=True)
    back_text = fields.Str(required=True)
    level = fields.Integer()
    fresh = fields.Bool()
    next = fields.DateTime(format=DATETIME_FORMAT)
    created = fields.DateTime(format=DATETIME_FORMAT)
    updated = fields.DateTime(format=DATETIME_FORMAT)
