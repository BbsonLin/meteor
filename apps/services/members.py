from apps.datacontracts.commands import CreateMemberCommand
from apps.datacontracts.commands import EditMemberCommand
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
    def create_member(self, command: CreateMemberCommand):
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
    def edit_member(self, command: EditMemberCommand):
        pass
    
    @transaction_scope
    def login(self, command: LoginCommand):
        pass

