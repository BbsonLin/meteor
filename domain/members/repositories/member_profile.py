import abc
from typing import List, Any
from domain.baseclass import PredicateSpecification
from domain.members.models import MemberProfileDO, MemberId


class IMemberProfileRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, member_profile_do: MemberProfileDO) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, member_profile_do: MemberProfileDO) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by(self, member_id: MemberId) -> MemberProfileDO:
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_id(self) -> MemberId:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by(self, find_pattern: PredicateSpecification) -> List[MemberProfileDO]:
        raise NotImplementedError()
