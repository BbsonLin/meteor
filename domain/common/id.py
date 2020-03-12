import abc
from datetime import datetime
from typing import TypeVar, Type, cast
from .valueobj import ValueObject


class EntityId(ValueObject):
    DATETIME_FORMAT = "%Y%m%d%H%M%S"

    @abc.abstractmethod
    def __init__(self, identifier: str) -> None:
        self._identifier = identifier

    @property
    def identifier(self) -> str:
        return self._identifier


    # def __eq__(self, other: object) -> bool:
    #     if type(self) is type(other):
    #         return False
    #     other = cast(EntityId, other)
    #     return (self.code, self.createtd_at, self.serial_no) == \
    #         (other.code, other.createtd_at, other.serial_no)

    # def __hash__(self) -> int:
    #     return hash((self.code, self.createtd_at, self.serial_no))

    # def __str__(self) -> str:
    #     # 取得字串型別的 Entity Id
    #     createtd_date = self.createtd_at.strftime(self.DATETIME_FORMAT)
    #     return "{code}-{date}-{sn}" \
    #         .format(code=self.code, date=createtd_date, sn=self.serial_no)

    # def __repr__(self) -> str:
    #     return "<{class}>: code={code}, createtd_at={date}, serial_no={sn}" \
    #         .format(type(self).__name__, code=self.code, date=self.createtd_at, sn=self.serial_no)

    # TODO: 實現 Iterable
