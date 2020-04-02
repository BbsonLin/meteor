from sqlalchemy import Column, String, Unicode
from infrastructures.persistences.sqlalchemy.models import CommSysInfo


class MemberProfile(CommSysInfo):
    __tablename__ = "member_profile"

    id = Column(String(255), primary_key=True)
    cellphone = Column(String(11), nullable=False)
    # 然後會員都是用身分證 + 手機為一組唯一來認，但不代表可以用同一組身分證外加多個手機開不同的銀行帳戶，因此事實上只是透過身分證來認
    # Unique
    identity_no = Column(String(20), nullable=False)
    family_name = Column(Unicode(45), nullable=False)
    given_name = Column(Unicode(45), nullable=False)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "<MemberProfile\n\
        id=%s\n\
        identity_no=%s\n\
        cellphone=%s\n\
        family_name=%s\n\
        given_name=%s>" % (
            self.id,
            self.identity_no,
            self.cellphone,
            self.family_name,
            self.given_name)
