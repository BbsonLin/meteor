from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class CreateMemberCmd(object):
    identity_no: str
    cellphone: str
    family_name: str
    given_name: str


@dataclass(frozen=True)
class EditMemberCmd(object):
    identity_no: Optional[str] = None
    cellphone: Optional[str] = None
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    is_deleted: Optional[bool] = None


@dataclass(frozen=True)
class GetMemberByIdCmd(object):
    member_id: str
