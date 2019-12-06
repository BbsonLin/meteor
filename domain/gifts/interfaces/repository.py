import abc
from domain.members.models.id import MemberId
from domain.gifts.models import GiftDO

class IGiftRepository(abc.ABC):
    @abc.abstractmethod
    def get_by(self, id: MemberId) -> GiftDO:
        raise NotImplementedError()