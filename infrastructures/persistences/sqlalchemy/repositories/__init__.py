from infrastructures.persistences.sqlalchemy.middlewares import db_adapter
from .member import MemberRepository


member_repository = MemberRepository(db_adapter.session)
