import traceback
from datetime import datetime
from typing import TypeVar, Type, cast
from domain.common import EntityId
from domain.common import DomainException
from domain.members.errors import MemberErrorCode


class MemberId(EntityId):
    code = "MEM"
    datetime_format = "%Y%m%d%H%M%S"

    def __init__(self, serial_no: int, createtd_at: datetime) -> None:
        # TODO: 客製化 Error Code 與 Message
        self._serial_no = self._check_serial_no(serial_no)
        self._createtd_at = createtd_at
        super(MemberId, self).__init__(self._make_identifier())

    @classmethod
    def translate(cls, source: str) -> "MemberId":
        CODE_IDX = 0
        CREATED_TIME_IDX = 1
        SERIAL_NO_IDX = 2

        if len(source.split("-")) != 3:
            raise DomainException(MemberErrorCode.MEMBER_ID_FORMAT_INCORRECT)

        slices = source.split("-")
        if slices[CODE_IDX] != cls.code:
            raise DomainException(MemberErrorCode.MEMBER_ID_FORMAT_INCORRECT)
        created_at = datetime.strptime(slices[CREATED_TIME_IDX], cls.datetime_format)
        return cls(int(slices[SERIAL_NO_IDX]), created_at)

    @property
    def serial_no(self) -> int:
        return self._serial_no

    @property
    def createtd_at(self) -> datetime:
        return self._createtd_at

    def _check_serial_no(self, serial_no: int) -> int:
        if serial_no < 0:
            raise DomainException(MemberErrorCode.MEMBER_SEIRAL_NO_INCORRECT, stack_trace=traceback.format_exc())
        return serial_no

    def _make_identifier(self):
        createtd_date = self.createtd_at.strftime(self.datetime_format)
        return "{code}-{date}-{sn}".format(code=self.code, date=createtd_date, sn=self.serial_no)

    def __eq__(self, other: object) -> bool:
        if type(self) is type(other):
            return False
        other = cast(MemberId, other)
        return (self.code, self.createtd_at, self.serial_no) == \
            (other.code, other.createtd_at, other.serial_no)

    def __hash__(self) -> int:
        return hash((self.code, self.createtd_at, self.serial_no))

    def __str__(self) -> str:
        # 取得字串型別的 Entity Id
        return self._make_identifier()

    def __repr__(self) -> str:
        return "<{class}: code={code}, createtd_at={date}, serial_no={sn}>" \
            .format(type(self).__name__, code=self.code, date=self.createtd_at, sn=self.serial_no)
