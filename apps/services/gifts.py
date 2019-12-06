from domain.gifts.models import GiftDO
from apps.datacontracts.results import GiftResult
from apps.datacontracts.commands import GetGiftByIdCommand
from infrastructures.persistences.sqlalchemy.repositories import GiftRepository
from domain.members.models import MemberId

class GiftService(object):
    def __init__(self, gift_repository: GiftRepository) -> None:
        self._gift_repo = gift_repository

    def get(self, command: GetGiftByIdCommand) -> GiftResult:
        # member_id: MemberId = MemberId.translate(command.member_id)
        member_id: MemberId = command.member_id
        gift: GiftDO = self._gift_repo.get_by(member_id)
        return GiftResult(
            gift_id = str(gift.gift_id),
            type = gift.type,
            type_name = gift.type_name,
            description = gift.description,
            invitation = {'code': gift.code, 'url': gift.url}
        )