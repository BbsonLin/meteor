from uuid import uuid1
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import false
from sqlalchemy.orm import Session
from domain.common import DomainException
from domain.members.models import MemberDO, MemberId
from domain.members.repositories import IMemberRepository
from domain.members.errors import MemberErrorCode
from infrastructures.persistences.sqlalchemy.models import Member


class MemberRepository(IMemberRepository):
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session

    def _assemble_to(self, db_member: Member) -> MemberDO:
        return MemberDO(
            id=MemberId.translate(db_member.id),
            identity_no=db_member.identity_no,
            cellphone=db_member.cellphone,
            family_name=db_member.family_name,
            given_name=db_member.given_name
        )

    def save(self, member: MemberDO) -> bool:
        args = {
            "id": str(member.id),
            "cellphone": member.cellphone,
            "identity_no": member.identity_no,
            "family_name": member.family_name,
            "given_name": member.given_name
        }
        db_member = Member(**args)
        self._db_session.add(db_member)
        self._db_session.flush()
        return True

    def get_by(self, mem_id: MemberId) -> MemberDO:
        db_member: Member = self._db_session.query(Member).filter(
            Member.id == str(mem_id),
            Member.is_deleted == false()
        ).scalar()

        if db_member is None:
            raise DomainException(MemberErrorCode.MEMBER_NOT_FOUND)

        return self._assemble_to(db_member)

    def generate_id(self) -> MemberId:
        return MemberId(uuid1())
