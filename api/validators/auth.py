from datetime import date
from decimal import Decimal
from marshmallow import Schema, fields, post_load, ValidationError


class UserLoginValidator(Schema):
    # "data_key" new naming of load_from and dump_to
    cellphone = fields.Int(data_key="cellphone", required=True)

    class Meta:
        strict = True
