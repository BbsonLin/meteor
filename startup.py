from typing import List, Optional
from starlette.applications import Starlette
from starlette.routing import BaseRoute, Mount
from api.resources import users
from settings import config, AppConfig
import uvicorn


class AppStartup(object):

    def __init__(self, config: AppConfig) -> None:
        self._routes: List[BaseRoute] = [
            Mount("/v1.0", routes=users.routes)
        ]
        self._app: Starlette = Starlette(debug=config.DEBUG,
                                         routes=self._routes)

    @property
    def instance(self) -> Starlette:
        return self._app

    @classmethod
    def boot(cls, config: AppConfig) -> Starlette:
        app = cls(config)
        return app.instance


app = AppStartup.boot(config)

# @app.route('/')
# async def hello(request):
#     return UJSONResponse({'hello': 'world'})
