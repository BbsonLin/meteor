import abc
from datetime import datetime
from typing import TypeVar, Type, cast
from .valueobj import ValueObject


class EntityId(ValueObject):
    DATETIME_FORMAT = "%Y%m%d%H%M%S"

    @abc.abstractmethod
    def __init__(self, code: str, serial_no: int, createtd_at: datetime) -> None:
        self._code = code
        # TODO: 客製化 Error Code 與 Message
        if serial_no < 0:
            raise ValueError("Serial No must larger than 0.")
        self._serial_no = serial_no
        self._createtd_at = createtd_at

    @classmethod
    def from_string(cls, entity_id: str):
        CODE_IDX = 0
        CREATED_IDX = 1
        SERIAL_NO_IDX = 2
        if len(entity_id.split("-")) != 3:
            raise Exception("Format Error !")

        slices = entity_id.split("-")
        created_at = datetime.strptime(slices[CREATED_IDX], cls.DATETIME_FORMAT)
        return cls(slices[CODE_IDX], int(slices[SERIAL_NO_IDX]), created_at)

    @property
    def code(self) -> str:
        return self._code

    @property
    def serial_no(self) -> int:
        return self._serial_no

    @property
    def createtd_at(self) -> datetime:
        return self._createtd_at

    def __eq__(self, other: object) -> bool:
        if type(self) is type(other):
            return False
        other = cast(EntityId, other)
        return (self.code, self.createtd_at, self.serial_no) == \
            (other.code, other.createtd_at, other.serial_no)

    def __hash__(self) -> int:
        return hash((self.code, self.createtd_at, self.serial_no))

    def __str__(self) -> str:
        # 取得字串型別的 Entity Id
        createtd_at = self.createtd_at.strftime(self.DATETIME_FORMAT)
        return "{code}-{date}-{sn}" \
            .format(code=self.code, date=self.createtd_at, sn=self.serial_no)

    def __repr__(self) -> str:
        return "<{class}>: code={code}, createtd_at={date}, serial_no={sn}" \
            .format(type(self).__name__, code=self.code, date=self.createtd_at, sn=self.serial_no)

    # TODO: 實現 Iterable
