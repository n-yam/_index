from marshmallow import Schema


# https://marshmallow.readthedocs.io/en/latest/examples.html#inflection-camel-casing-keys


class CamelCaseSchema(Schema):

    def camelcase(self, s):
        parts = iter(s.split("_"))
        return next(parts) + "".join(i.title() for i in parts)

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = self.camelcase(field_obj.data_key or field_name)
