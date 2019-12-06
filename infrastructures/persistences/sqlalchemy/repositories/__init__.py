from .gift import GiftRepository
from infrastructures.persistences.sqlalchemy.middlewares import db_adapter
from .member import MemberRepository


member_repository = MemberRepository(db_adapter.session)
gift_repository = GiftRepository(db_adapter.session)
