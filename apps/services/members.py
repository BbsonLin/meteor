from apps.datacontracts.commands import CreateMemberCommand
from apps.datacontracts.commands import EditMemberCommand
from apps.datacontracts.commands import GetMemberByIdCommand
from apps.datacontracts.commands import LoginCommand
from apps.datacontracts.results import MemberResult
from apps.datacontracts.results import MemberLoginResult
from domain.members.models import MemberDO, MemberId
from infrastructures.persistences.sqlalchemy.repositories import MemberRepository
from infrastructures.persistences.sqlalchemy.middlewares import transaction_scope


class MemberService(object):
    def __init__(self, member_repository: MemberRepository) -> None:
        self._member_repo = member_repository

    @transaction_scope
    def create(self, command: CreateMemberCommand) -> MemberResult:
        member_id: MemberId = self._member_repo.generate_id()
        member = MemberDO(member_id,
                          command.identity,
                          command.cellphone,
                          command.family_name,
                          command.given_name)
        self._member_repo.save(member)
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
        member: MemberDO = self._member_repo.get_by(member_id)
        return MemberResult(
            member_id=str(member.id),
            identity=member.identity,
            cellphone=member.cellphone,
            family_name=member.family_name,
            given_name=member.given_name
        )
