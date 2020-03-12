from typing import Sequence, Optional, Any, Union
from starlette.applications import Starlette
from starlette.routing import BaseRoute, Mount, Route
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette_context.plugins import RequestIdPlugin
from starlette_context.middleware import ContextMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from api.resources.members import members_profile_routes
from api.resources.auth import member_auth_routes
from infrastructures.errors import ExceptHandlerMiddleware
from infrastructures.persistences.sqlalchemy.middlewares import database_adapter, SQLAlchemyAdapter
from infrastructures.persistences.sqlalchemy.middlewares import SQLAlchemySessionMiddleware
from settings import app_config, AppConfig


class AppStartup(object):

    def __init__(self, config: AppConfig, database_adapter: SQLAlchemyAdapter, except_handlers=None) -> None:
        self._database_adapter = database_adapter
        self._middlewares: Sequence[Middleware] = self._register_middleware(config)
        self._routes: Sequence[BaseRoute] = self._register_routers()
        # starlette custom exception_handlers will work when debug mode is False
        self._app: Starlette = Starlette(debug=config.DEBUG,
                                         routes=self._routes,
                                         middleware=self._middlewares,
                                         exception_handlers=except_handlers)

    def _register_routers(self) -> Sequence[BaseRoute]:
        app_routes: Sequence[BaseRoute] = [
            Mount("/v1.0", routes=[
                members_profile_routes,
                member_auth_routes
            ])
        ]
        return app_routes

    def _register_middleware(self, config: AppConfig) -> Sequence[Middleware]:
        middleware: Sequence[Middleware] = [
            Middleware(TrustedHostMiddleware, allowed_hosts=config.ALLOWED_HOSTS),
            Middleware(CORSMiddleware, allow_origins=config.ALLOW_ORIGINS),
            Middleware(ContextMiddleware.with_plugins(RequestIdPlugin)),
            Middleware(ExceptHandlerMiddleware),
            Middleware(SQLAlchemySessionMiddleware, alchemy=self._database_adapter),
            # TODO 請加入 HTTPSRedirectMiddleware 與 SessionMiddleware (若需要 secret_key，已放在參考設定檔)
        ]
        return middleware

    @property
    def instance(self) -> Starlette:
        return self._app

    @classmethod
    def boot(cls, config: AppConfig, database_adapter: SQLAlchemyAdapter, except_handlers=None) -> Starlette:
        app = cls(config, database_adapter, except_handlers)
        return app.instance


app = AppStartup.boot(app_config, database_adapter)
