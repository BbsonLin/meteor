
from apps.datacontracts.commands.members import MemberLoginCmd
from apps.datacontracts.results.members import MemberLoginRst
from apps.repositories.members import MemberProfileRepository
from domain.members.models import MemberProfileDO, MemberId
from infrastructures.persistences.sqlalchemy.middlewares import database_adapter
from infrastructures.persistences.sqlalchemy.middlewares import transaction_scope


class MemberAuthenticationService(object):
    _member_repository: MemberProfileRepository = MemberProfileRepository(database_adapter.session)

    def __init__(self) -> None:
        pass

    @transaction_scope
    def login(self, command: MemberLoginCmd):
        pass


member_auth_service = MemberAuthenticationService()
