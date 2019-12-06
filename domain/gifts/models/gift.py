from datetime import datetime
from typing import Optional
from domain.members.models.id import MemberId

class GiftDO(object):
    def __init__(self, gift_id: str, type: str, type_name: str, description: str, code: str, url: str) -> None:
        self._gift_id = gift_id
        self._type = type
        self._type_name = type_name
        self._description = description
        self._code = code
        self._url = url

    @property
    def gift_id(self) -> str:
        return self._gift_id
    
    @property
    def type(self) -> str:
        return self._type

    @property
    def type_name(self) -> str:
        return self._type_name
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def code(self) -> str:
        return self._code
    
    @property
    def url(self) -> str:
        return self._url

   

    def __repr__(self) -> str:
        return "<MemberDO: id:{}>" \
            .format(self.id)
