from functools import wraps
from settings import app_config
from sqlalchemy.orm import Session
from .middlewares import SQLAlchemyAdapter
from .repositories import MemberRepository



# def transaction(func):
#     @wraps(func)
#     def decorator(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             session.commit()
#             return result
#         except Exception as e:
#             session.rollback()
#     return decorator
