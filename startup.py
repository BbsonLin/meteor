from typing import List, Optional, Any, Union
from starlette.applications import Starlette
from starlette.routing import BaseRoute, Mount, Route
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from api.resources.members import member_router, members_router
from api.resources.gifts import gifts_router
from api.resources.auth import login_router
from infrastructures.errors import ExceptHandlerMiddleware
from infrastructures.persistences.sqlalchemy.middlewares import db_adapter, SQLAlchemyAdapter
from infrastructures.persistences.sqlalchemy.middlewares import SQLAlchemySessionMiddleware
from settings import app_config, AppConfig


class AppStartup(object):

    def __init__(self, config: AppConfig, database_adapter: SQLAlchemyAdapter, except_handlers=None) -> None:
        self._database_adapter = database_adapter
        self._middlewares: List[Optional[Middleware]] = self._register_middleware(config)
        self._routes: List[BaseRoute] = self._register_routers()
        # starlette custom exception_handlers will work when debug mode is False
        self._app: Starlette = Starlette(debug=config.DEBUG,
                                         routes=self._routes,
                                         middleware=self._middlewares,
                                         exception_handlers=except_handlers)

    def _register_routers(self) -> List[BaseRoute]:
        app_routes: List[BaseRoute] = [
            Mount("/v1.0", routes=[
                members_router,
                member_router,
                login_router,
                gifts_router
            ])
        ]
        return app_routes

    def _register_middleware(self, config: AppConfig) -> List[Optional[Middleware]]:
        middleware: List[Optional[Middleware]] = [
            Middleware(TrustedHostMiddleware, allowed_hosts=config.ALLOWED_HOSTS),
            Middleware(CORSMiddleware, allow_origins=config.ALLOW_ORIGINS),
            Middleware(ExceptHandlerMiddleware),
            Middleware(SQLAlchemySessionMiddleware, alchemy=self._database_adapter),
            # TODO 請加入 HTTPSRedirectMiddleware 與 SessionMiddleware (若需要 secret_key，已放在參考設定檔)
        ]
        return middleware

    @property
    def instance(self) -> Starlette:
        return self._app

    @classmethod
    def boot(cls, config: AppConfig, db_adapter: SQLAlchemyAdapter, except_handlers=None) -> Starlette:
        app = cls(config, db_adapter, except_handlers)
        return app.instance


app = AppStartup.boot(app_config, db_adapter)
