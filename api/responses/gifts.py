from datetime import date
from decimal import Decimal
from marshmallow import fields
from packages.marshmallow import DumpSchema

class GiftResponse(DumpSchema):
    gift_id = fields.String(data_key="gift_id", dump_only=True)
    type = fields.String(data_key="type", dump_only=True)
    type_name = fields.String(data_key="type_name", dump_only=True)
    description = fields.String(data_key="description", dump_only=True)
    invitation = fields.String(data_key="invitation", dump_only=True)

    class Meta:
        strict = True