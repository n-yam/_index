from marshmallow import fields

from index.camel_case_schema import CamelCaseSchema


class CardSchema(CamelCaseSchema):
    id = fields.Int()
    front_text = fields.Str(required=True)
    back_text = fields.Str(required=True)
