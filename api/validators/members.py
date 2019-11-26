from datetime import date
from decimal import Decimal
from marshmallow import Schema, fields, post_load, ValidationError


class CreateMemberValidator(Schema):
    # "data_key" new naming of load_from and dump_to
    identity = fields.String(data_key="identity", required=True)
    cellphone = fields.String(data_key="cellphone", required=True)
    family_name = fields.String(data_key="family_name", required=True)
    given_name = fields.String(data_key="given_name", required=True)

    class Meta:
        strict = True


class EditMemberValidator(Schema):
    # "data_key" new naming of load_from and dump_to
    identity = fields.Decimal(data_key="identity")
    cellphone = fields.Int(data_key="cellphone")
    family_name = fields.String(data_key="family_name")
    given_name = fields.String(data_key="given_name")
    is_archived = fields.Boolean(data_key="is_archived")

    class Meta:
        strict = True
