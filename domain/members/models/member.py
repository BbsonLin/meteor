from typing import Optional
from datetime import datetime
from .id import MemberId


class MemberDO(object):
    def __init__(self, id: MemberId, identity: str, cellphone: str, family_name: str, given_name: str) -> None:
        self._id = id
        self._identity = identity
        self._cellphone = cellphone
        self._family_name = family_name
        self._given_name = given_name

    @property
    def id(self) -> MemberId:
        return self._id

    @property
    def identity(self) -> str:
        return self._identity

    @property
    def cellphone(self) -> str:
        return self._cellphone

    @property
    def family_name(self) -> str:
        return self._family_name

    @property
    def given_name(self) -> str:
        return self._given_name

    def edit_cellpone(self, cellphone: Optional[str]):
        if cellphone:
            self._cellphone = cellphone

    def change_identity(self, identity: Optional[str]):
        if identity:
            self._identity = identity

    def __eq__(self, other: object) -> bool:
        # 使用 is 判斷引用是否一致，等同 id(self) == id(other)，半段引用的記憶體位置，此外因為是可改變狀態，所以不用覆寫 __hash__
        if type(self) != type(other):
            return False
        return self is other

    def __repr__(self) -> str:
        return "<MemberDO: id:{}, \n\
                identity={}, \n\
                cellphone={}, \n\
                family_name={}, \n\
                given_name={}>" \
            .format(self.id,
                    self.identity,
                    self.cellphone,
                    self.family_name,
                    self.given_name)
