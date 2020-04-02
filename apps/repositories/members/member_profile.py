from uuid import uuid1
from typing import List, Any
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import false
from sqlalchemy.orm import Session
from domain.baseclass import DomainException, PredicateSpecification
from domain.members.models import MemberProfileDO, MemberId
from domain.members.repositories import IMemberProfileRepository
from domain.members.errors import MemberErrorCode
from infrastructures.persistences.sqlalchemy.models import MemberProfile
from infrastructures.persistences.sqlalchemy.middlewares import database_adapter


class MemberProfileRepository(IMemberProfileRepository):
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session

    def _assemble_do(self, db_member: MemberProfile) -> MemberProfileDO:
        return MemberProfileDO(
            id=MemberId.translate(db_member.id),
            identity_no=db_member.identity_no,
            cellphone=db_member.cellphone,
            family_name=db_member.family_name,
            given_name=db_member.given_name
        )

    def save(self, member_do: MemberProfileDO) -> None:
        create_args = {
            "id": str(member_do.id),
            "cellphone": member_do.cellphone,
            "identity_no": member_do.identity_no,
            "family_name": member_do.family_name,
            "given_name": member_do.given_name
        }
        db_member = MemberProfile(**create_args)
        self._db_session.add(db_member)
        self._db_session.flush()

    def update(self, member_do: MemberProfileDO) -> None:
        db_member: MemberProfile = self._db_session.query(MemberProfile).filter(
            MemberProfile.id == str(member_do.id),
            MemberProfile.is_deleted == false()
        ).scalar()

        if db_member is None:
            raise DomainException(MemberErrorCode.MEMBER_NOT_FOUND)

        db_member.id = str(member_do.id)
        db_member.cellphone = member_do.cellphone
        db_member.identity_no = member_do.identity_no
        db_member.family_name = member_do.family_name
        db_member.given_name = member_do.given_name
        self._db_session.flush()

    def get_by(self, member_id: MemberId) -> MemberProfileDO:
        db_member: MemberProfile = self._db_session.query(MemberProfile).filter(
            MemberProfile.id == str(member_id),
            MemberProfile.is_deleted == false()
        ).scalar()

        if db_member is None:
            raise DomainException(MemberErrorCode.MEMBER_NOT_FOUND)

        return self._assemble_do(db_member)

    def generate_id(self) -> MemberId:
        return MemberId(uuid1())

    def find_by(self, sepcification: PredicateSpecification) -> List[MemberProfileDO]:
        predicate = sepcification(MemberProfileDO)
        members_do = self._db_session.query(MemberProfileDO).filter(predicate).all()
        return [
            self._assemble_do(member_do)
            for member_do in members_do
        ]


member_profile_repository = MemberProfileRepository(database_adapter.session)
