import abc
from domain.members.models import MemberDO, MemberId


class IMemberRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, order: MemberDO) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by(self, id: MemberId) -> MemberDO:
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_id(self) -> MemberId:
        raise NotImplementedError()
