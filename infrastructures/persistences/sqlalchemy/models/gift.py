from sqlalchemy import Column, String, Unicode
from .common import SystemInfo

class Gift(SystemInfo):
    __tablename__ = "gifts"

    gift_id = Column(String(255), primary_key=True)
    member_id = Column(String(255), nullable=False)
    type = Column(String(1), nullable=False)
    type_name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    code = Column(String(10), nullable=False)
    url = Column(String(255), nullable=False)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "<gift_id\n\
        member_id=%s\n\
        type=%s\n\
        type_name=%s\n\
        cellphone=%s\n\
        description=%s\n\
        code=%s\n\
        url=%s>" % (
            self.gift_id,
            self.member_id,
            self.type,
            self.type_name,
            self.description,
            self.code,
            self.url)

