from marshmallow import Schema, fields
from models.address import Address


class AddressSchema(Schema):
    class Meta:
        model = Address

    street = fields.String()
    city = fields.String()
    state = fields.String()
    postal_code = fields.Integer()
