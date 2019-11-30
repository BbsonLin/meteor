from sqlalchemy.orm import Session
from domain.members.models import Member, MemberId
from domain.members.interfaces import IMemberRepository


class MemberRepository(IMemberRepository):
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session

    def save(self, member: Member) -> None:
        pass

    def get_by(self, member: MemberId) -> Member:
        pass

    def generate_id(self) -> MemberId:
        pass
