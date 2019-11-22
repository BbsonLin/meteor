from marshmallow import Schema, post_dump


class DumpSchema(Schema):
    @post_dump
    def clean(self, data):
        return {key: val for key, val in data.items() if val is not None}