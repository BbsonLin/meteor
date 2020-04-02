from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean, String
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

Base: DeclarativeMeta = declarative_base()


class CommSysInfo(Base):
    """
    Abstract Model, for every model used
    """
    __abstract__ = True

    # utc get utf time, if need local time, please call now()
    created_at = Column(DateTime,
                        default=datetime.utcnow,
                        nullable=False)
    updated_at = Column(DateTime,
                        onupdate=datetime.utcnow,
                        nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    # mark data was deleted
    is_deleted = Column(Boolean, default=False, nullable=False)
    # who operating this data
    operator_seq = Column(String(40), nullable=True)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __repr__(self):
        return "<SystemInfo: \n\
            created_at:%s\n\
            updated_at=%s\n\
            deleted_at=%s\n\
            is_deleted=%s\n\
            operator_seq=%s>" % (self.created_at,
                                 self.updated_at,
                                 self.deleted_at,
                                 self.is_deleted,
                                 self.operator_seq)
