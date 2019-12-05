from domain.common import DomainErrorCode


class MemberErrorCode(DomainErrorCode):
    MEMBER_ID_FORMAT_INCORRECT = "Member id format does not incorrect"
    MEMBER_NOT_FOUND = "Member does not found"
    MEMBER_SEIRAL_NO_INCORRECT = "Member serial No must be larger than 0"
