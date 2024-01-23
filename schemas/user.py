from marshmallow import Schema, fields
from models.user import User
from schemas.address import AddressSchema
from schemas.phone_number import PhoneNumberSchema


class UserSchema(Schema):
    class Meta:
        model = User

    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    gender = fields.String()
    age = fields.Integer()
    address = fields.Nested(AddressSchema, many=True)
    phone_numbers = fields.Nested(PhoneNumberSchema, many=True)

