import traceback
from uuid import UUID
from datetime import datetime
from typing import TypeVar, Type, cast
from domain.common import EntityId
from domain.common import DomainException
from domain.members.errors import MemberErrorCode


class MemberId(EntityId):
    code = "MEM"

    def __init__(self, uuid: UUID) -> None:
        # TODO: 客製化 Error Code 與 Message
        self._uuid = uuid
        super(MemberId, self).__init__(self._make_identifier())

    @classmethod
    def translate(cls, source: str) -> "MemberId":
        TOTAL_SIZE, CODE_SIZE = 35, 3
        if len(source) != TOTAL_SIZE or source[:CODE_SIZE] != cls.code:
            raise DomainException(MemberErrorCode.MEMBER_ID_FORMAT_ERROR)

        uuid_slice = source[CODE_SIZE:]
        return cls(UUID(uuid_slice))

    @property
    def uuid(self) -> UUID:
        return self._uuid

    def _make_identifier(self):
        uuid_hex = self.uuid.hex
        return "{code}{uuid_hex}".format(code=self.code, uuid_hex=uuid_hex)

    def __eq__(self, other: object) -> bool:
        if type(self) is type(other):
            return False
        other = cast(MemberId, other)
        return (self.code, self.uuid) == (other.code, other.uuid)

    def __hash__(self) -> int:
        return hash((self.code, self.uuid))

    def __str__(self) -> str:
        # 取得字串型別的 Entity Id
        return self._make_identifier()

    def __repr__(self) -> str:
        return "<{class_name}: code={code}, uuid_hex={uuid_hex}>" \
            .format(class_name=type(self).__name__,
                    code=self.code,
                    uuid_hex=self.uuid)
