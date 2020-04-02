from dataclasses import dataclass



@dataclass(frozen=True)
class MemberLoginRst(object):
    member_id: str
    invitation_code: str
