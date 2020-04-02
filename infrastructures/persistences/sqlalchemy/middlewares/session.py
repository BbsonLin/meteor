from settings import DatabaseConfig
from .adapter import SQLAlchemyAdapter
from starlette.middleware.base import BaseHTTPMiddleware, ASGIApp
import traceback

class SQLAlchemySessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, alchemy: SQLAlchemyAdapter):
        super().__init__(app)
        self._alchemy = alchemy

    async def dispatch(self, request, call_next):
        try:
            self._alchemy.register_session()
            response = await call_next(request)
            self._alchemy.remove_session()
            return response
        except Exception as dex:
            # 發生例外後移除 Session 來釋放咬著的 transaction 與 connection 資源 (返回 pool)
            self._alchemy.remove_session()
            raise dex
