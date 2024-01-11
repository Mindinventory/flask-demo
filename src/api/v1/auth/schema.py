from marshmallow import Schema, fields


class Login(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class UserResponse(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()