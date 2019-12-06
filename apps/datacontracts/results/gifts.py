from dataclasses import dataclass


@dataclass(frozen=True)
class GiftResult(object):
    gift_id: str
    type: str
    type_name: str
    description: str
    invitation: dict