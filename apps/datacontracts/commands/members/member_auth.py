from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class MemberLoginCmd(object):
    cellphone: str
