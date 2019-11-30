from typing import Any
from functools import wraps
from .adapter import db_adapter
from sqlalchemy.orm.session import Session


def transaction_scope(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            db_adapter.session.commit()
            return result
        except Exception as ex:
            db_adapter.session.rollback()
            raise ex
    return decorator
