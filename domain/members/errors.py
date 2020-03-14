from domain.common import DomainErrorCode


class MemberErrorCode(DomainErrorCode):
    MEMBER_ID_FORMAT_ERROR = "Member id format was error"
    MEMBER_NOT_FOUND = "Member does not found"
