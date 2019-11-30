from settings import DatabaseConfig
from .adapter import SQLAlchemyAdapter
from starlette.middleware.base import BaseHTTPMiddleware


class SQLAlchemySessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, alchemy: SQLAlchemyAdapter):
        super().__init__(app)
        self._alchemy = alchemy

    async def dispatch(self, request, call_next):
        self._alchemy.register_session()
        response = await call_next(request)
        self._alchemy.remove_session()
        return response
