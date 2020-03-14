from dataclasses import dataclass


@dataclass(frozen=True)
class MemberProfileRst(object):
    member_id: str
    identity_no: str
    cellphone: str
    family_name: str
    given_name: str
