from marshmallow import Schema, fields
from models.phone_number import PhoneNumber


class PhoneNumberSchema(Schema):
    class Meta:
        model = PhoneNumber

    id = fields.Integer()
    type = fields.String()
    number = fields.Integer()
