from datetime import datetime
from sqlalchemy import func
from sqlalchemy.sql.expression import false
from sqlalchemy.orm import Session
from domain.members.models import MemberDO, MemberId
from domain.members.interfaces import IMemberRepository
from infrastructures.persistences.sqlalchemy.models import Member


class MemberRepository(IMemberRepository):
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session

    def _transfer_to(self, db_member: Member) -> MemberDO:
        return MemberDO(
            id=MemberId.from_string(db_member.member_id),
            identity=db_member.identity,
            cellphone=db_member.cellphone,
            family_name=db_member.family_name,
            given_name=db_member.given_name
        )

    def save(self, member: MemberDO) -> bool:
        args = {
            "member_id": str(member.id),
            "cellphone": member.cellphone,
            "identity": member.identity,
            "family_name": member.family_name,
            "given_name": member.given_name
        }
        db_member = Member(**args)
        self._db_session.add(db_member)
        self._db_session.flush()
        return True

    def get_by(self, member_id: MemberId) -> MemberDO:
        db_member: Member = self._db_session.query(Member).filter(
            Member.member_id == str(member_id),
            Member.is_archived == false()
        ).scalar()

        if db_member is None:
            raise Exception("Member Not Found")

        return self._transfer_to(db_member)

    def generate_id(self) -> MemberId:
        max_id = self._db_session.query(func.max(Member.member_id)).scalar()
        # 如果 為 NONE 表示沒有資料，則建立 0
        curr_id = max_id + 1 if max_id is not None else 0
        return MemberId(curr_id, datetime.utcnow())
