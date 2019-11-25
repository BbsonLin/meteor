from apps.datacontracts.commands import CreateMemberCommand
from apps.datacontracts.commands import EditMemberCommand
from apps.datacontracts.commands import LoginCommand
from apps.datacontracts.results import MemberResult
from apps.datacontracts.results import MemberLoginResult
from domain.members.models import Member, MemberId


class MemberService(object):
    def __init__(self):
        pass

    def create_member(self, command: CreateMemberCommand):
        try:
            # member_id: MemberId = self._order_repo.generate_id()
            # order = Member(member_id,
            #                command.identity,
            #                command.cellphone,
            #                command.family_name,
            #                command.cellphone)
            # self._order_repo.save(order)
            # self._session.commit()
            return True
            # return CreatedOrderAssembler.to_result(order)
        except Exception as e:
            # self._session.rollback()
            raise e

    def edit_member(self, command: EditMemberCommand):
        pass

    def login(self, command: LoginCommand):
        pass
