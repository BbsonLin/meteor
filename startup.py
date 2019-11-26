from typing import List, Optional
from starlette.applications import Starlette
from starlette.routing import BaseRoute, Mount, Route
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from api.resources.members import member_router, members_router
from settings import config, AppConfig


class AppStartup(object):

    def __init__(self, config: AppConfig) -> None:
        self._middlewares: List[Optional[Middleware]] = self._register_middleware(config)
        self._routes: List[BaseRoute] = self._register_routers()
        self._app: Starlette = Starlette(debug=config.DEBUG,
                                         routes=self._routes,
                                         middleware=self._middlewares)

    def _register_routers(self) -> List[BaseRoute]:
        app_routes: List[BaseRoute] = [
            Mount("/v1.0", routes=[
                members_router,
                member_router
            ])
        ]
        return app_routes

    def _register_middleware(self, config: AppConfig) -> List[Optional[Middleware]]:
        middleware: List[Optional[Middleware]] = [
            Middleware(TrustedHostMiddleware, allowed_hosts=config.ALLOWED_HOSTS),
            Middleware(CORSMiddleware, allow_origins=config.ALLOW_ORIGINS),
            # TODO 請加入 HTTPSRedirectMiddleware 與 SessionMiddleware (若需要 secret_key，已放在參考設定檔)
        ]
        return middleware

    @property
    def instance(self) -> Starlette:
        return self._app

    @classmethod
    def boot(cls, config: AppConfig) -> Starlette:
        app = cls(config)
        return app.instance


app = AppStartup.boot(config)
