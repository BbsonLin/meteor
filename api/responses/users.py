from datetime import date
from decimal import Decimal
from marshmallow import fields
from packages.marshmallow import DumpSchema


class UserResponse(DumpSchema):
    user_id = fields.UUID(data_key="user_id", dump_only=True)
    identity = fields.Decimal(data_key="identity", dump_only=True)
    cellphone = fields.Int(data_key="cellphone", dump_only=True)
    family_name = fields.String(data_key="family_name", dump_only=True)
    given_name = fields.String(data_key="given_name", dump_only=True)

    class Meta:
        strict = True

