from dataclasses import dataclass


@dataclass(frozen=True)
class MemberResult(object):
    member_id: str
    identity: str
    cellphone: str
    family_name: str
    given_name: str


@dataclass(frozen=True)
class MemberLoginResult(object):
    member_id: str
    invitation_code: str
