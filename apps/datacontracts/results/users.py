from dataclasses import dataclass


@dataclass(frozen=True)
class UserResult(object):
    user_id: str
    identity: str
    cellphone: str
    family_name: str
    given_name: str


@dataclass(frozen=True)
class UserLoginResult(object):
    user_id: str
    invitation_code: str
