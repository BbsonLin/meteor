from apps.datacontracts.commands.members import CreateMemberCmd
from apps.datacontracts.commands.members import EditMemberCmd
from apps.datacontracts.commands.members import GetMemberByIdCmd
from apps.datacontracts.commands.members import MemberLoginCmd
from apps.datacontracts.results.members import MemberProfileRst
from apps.datacontracts.results.members import MemberLoginRst
from apps.repositories.members import MemberProfileRepository
from domain.members.models import MemberProfileDO, MemberId
from infrastructures.persistences.sqlalchemy.middlewares import database_adapter
from infrastructures.persistences.sqlalchemy.middlewares import transaction_scope


class MemberProfileService(object):
    _member_repository: MemberProfileRepository = MemberProfileRepository(database_adapter.session)

    def __init__(self) -> None:
        pass

    @transaction_scope
    def create(self, command: CreateMemberCmd) -> MemberProfileRst:
        member_id: MemberId = self._member_repository.generate_id()
        member = MemberProfileDO(member_id,
                                 command.identity_no,
                                 command.cellphone,
                                 command.family_name,
                                 command.given_name)
        self._member_repository.save(member)
        return MemberProfileRst(
            member_id=str(member_id),
            identity_no=command.identity_no,
            cellphone=command.cellphone,
            family_name=command.family_name,
            given_name=command.given_name
        )

    @transaction_scope
    def edit(self, command: EditMemberCmd):
        pass

    def get(self, command: GetMemberByIdCmd) -> MemberProfileRst:
        member_id: MemberId = MemberId.translate(command.member_id)
        member: MemberProfileDO = self._member_repository.get_by(member_id)
        return MemberProfileRst(
            member_id=str(member.id),
            identity_no=member.identity_no,
            cellphone=member.cellphone,
            family_name=member.family_name,
            given_name=member.given_name
        )


member_profile_service = MemberProfileService()
