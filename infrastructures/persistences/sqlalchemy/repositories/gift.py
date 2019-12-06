from typing import List
from sqlalchemy.orm import Session
from domain.members.models import MemberId
from domain.gifts.models import GiftDO
from domain.gifts.interfaces import IGiftRepository
from infrastructures.persistences.sqlalchemy.models import Gift

class GiftRepository(IGiftRepository):
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session
    
    def _assemble_to(self, db_gift: Gift) -> GiftDO:
        return GiftDO(
            gift_id = db_gift.gift_id,
            type = db_gift.type,
            type_name = db_gift.type_name,
            description = db_gift.description,
            code = db_gift.code,
            url = db_gift.url
        )

    def get_by(self, member_id: MemberId) -> GiftDO:
        db_gift: List[Gift] = self._db_session.query(Gift).filter(
            Gift.member_id == str(member_id),
            Gift.is_archived == false()
        ).all()

        # if db_gift is None:
        #     raise Exception("Gift Not Found")
        db_gift = GiftDO(
            gift_id = 'db_gift.gift_id',
            type = 'db_gift.type',
            type_name = 'db_gift.type_name',
            description = 'db_gift.description',
            code = 'db_gift.code',
            url = 'db_gift.url'
        )
        return self._assemble_to(db_gift)