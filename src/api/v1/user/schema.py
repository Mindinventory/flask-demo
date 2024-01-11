from marshmallow import Schema, fields, validates, ValidationError


class UserCreate(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

    @validates('username')
    def validate_username(self, value):
        if not value.isalnum():
            raise ValidationError('Username must contain only letters and numbers.')


class UserUpdate(Schema):
    first_name = fields.Str()
    last_name = fields.Str()


class UserResponse(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()