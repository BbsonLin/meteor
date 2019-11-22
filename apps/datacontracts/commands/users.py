from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserCommand(object):
    identity: str
    cellphone: str
    family_name: str
    given_name: str


@dataclass(frozen=True)
class EditUserCommand(object):
    identity: Optional[str] = None
    cellphone: Optional[str] = None
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    is_archived: Optional[bool] = None


@dataclass(frozen=True)
class LoginCommand(object):
    cellphone: str
