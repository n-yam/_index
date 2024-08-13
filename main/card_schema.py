from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from main.card import Card


class CardSchema(SQLAlchemySchema):
    class Meta:
        model = Card
        load_instance = True

    card_id = auto_field()
    front_text = auto_field()
    back_text = auto_field()
