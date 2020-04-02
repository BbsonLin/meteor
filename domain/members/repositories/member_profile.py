import abc
from domain.members.models import MemberProfileDO, MemberId


class IMemberProfileRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, order: MemberProfileDO) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by(self, id: MemberId) -> MemberProfileDO:
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_id(self) -> MemberId:
        raise NotImplementedError()
