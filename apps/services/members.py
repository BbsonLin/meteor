from apps.datacontracts.commands import CreateMemberCommand
from apps.datacontracts.commands import EditMemberCommand
from apps.datacontracts.commands import GetMemberByIdCommand
from apps.datacontracts.commands import LoginCommand
from apps.datacontracts.results import MemberResult
from apps.datacontracts.results import MemberLoginResult
from apps.repositories.member import MemberRepository
from domain.members.models import MemberDO, MemberId
from infrastructures.persistences.sqlalchemy.middlewares import database_adapter
from infrastructures.persistences.sqlalchemy.middlewares import transaction_scope


class MemberProfileService(object):
    _member_repository: MemberRepository = MemberRepository(database_adapter.session)

    def __init__(self) -> None:
        pass

    @transaction_scope
    def create(self, command: CreateMemberCommand) -> MemberResult:
        member_id: MemberId = self._member_repository.generate_id()
        member = MemberDO(member_id,
                          command.identity,
                          command.cellphone,
                          command.family_name,
                          command.given_name)
        self._member_repository.save(member)
        return MemberResult(
            member_id=str(member_id),
            identity=command.identity,
            cellphone=command.cellphone,
            family_name=command.family_name,
            given_name=command.given_name
        )

    @transaction_scope
    def edit(self, command: EditMemberCommand):
        pass

    @transaction_scope
    def login(self, command: LoginCommand):
        pass

    def get(self, command: GetMemberByIdCommand) -> MemberResult:
        member_id: MemberId = MemberId.translate(command.member_id)
        member: MemberDO = self._member_repository.get_by(member_id)
        return MemberResult(
            member_id=str(member.id),
            identity=member.identity,
            cellphone=member.cellphone,
            family_name=member.family_name,
            given_name=member.given_name
        )


member_service = MemberProfileService()
