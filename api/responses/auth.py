from datetime import date
from decimal import Decimal
from marshmallow import fields
from packages.marshmallow import DumpSchema


class MemberLoginResponse(DumpSchema):
    cellphone = fields.UUID(data_key="cellphone", dump_only=True)

    class Meta:
        strict = True


