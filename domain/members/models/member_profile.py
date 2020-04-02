from typing import Optional, cast
from datetime import datetime
from .member_id import MemberId


class MemberProfileDO(object):
    def __init__(self,
                 id: MemberId,
                 identity_no: str,
                 cellphone: str,
                 family_name: str,
                 given_name: str) -> None:

        self._id = id
        self._identity_no = identity_no
        self._cellphone = cellphone
        self._family_name = family_name
        self._given_name = given_name

    @property
    def id(self) -> MemberId:
        return self._id

    @property
    def identity_no(self) -> str:
        return self._identity_no

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

    def change_identity_no(self, identity_no: Optional[str]):
        if identity_no:
            self._identity_no = identity_no

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return False
        # 使用 is 判斷引用是否一致，等同 id(self) == id(other)，判斷引用的記憶體位置，此外因為是可改變狀態，所以不用覆寫 __hash__
        return self is other

    def __repr__(self) -> str:
        return "<MemberProfileDO: id:{}, \n\
                identity_no={}, \n\
                cellphone={}, \n\
                family_name={}, \n\
                given_name={}>" \
            .format(self.id,
                    self.identity_no,
                    self.cellphone,
                    self.family_name,
                    self.given_name)
