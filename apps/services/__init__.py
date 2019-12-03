from infrastructures.persistences.sqlalchemy.repositories import member_repository
from .members import MemberService


member_service = MemberService(member_repository)
