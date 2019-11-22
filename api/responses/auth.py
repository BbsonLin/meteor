from datetime import date
from decimal import Decimal
from marshmallow import fields
from packages.marshmallow import DumpSchema


class UserLoginResponse(DumpSchema):
    user_id = fields.UUID(data_key="user_id", dump_only=True)
    invitation_code = fields.UUID(data_key="invitation_code", dump_only=True)

    class Meta:
        strict = True


