from datetime import datetime
from domain.common import EntityId


class MemberId(EntityId):
    def __init__(self, id: int, createtd_at: datetime) -> None:
        super(MemberId, self).__init__("MEM", id, createtd_at)
