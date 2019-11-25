from domain.members.models import Member, MemberId
from domain.members.interfaces import IMemberRepository


class MemberRepository(IMemberRepository):

    def save(self, member: Member) -> bool:
        raise NotImplementedError()

    def get_by(self, id: MemberId) -> Member:
        raise NotImplementedError()

    def generate_id(self) -> MemberId:
        raise NotImplementedError()
