from typing import Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class GetGiftByIdCommand(object):
    member_id: str