import abc
from domain.members.models import Member, MemberId


class IMemberRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, order: Member) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by(self, id: MemberId) -> Member:
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_id(self) -> MemberId:
        raise NotImplementedError()
