from infrastructures.persistences.sqlalchemy.repositories import member_repository, gift_repository
from .members import MemberService
from .gifts import GiftService


member_service = MemberService(member_repository)
gift_service = GiftService(gift_repository)
