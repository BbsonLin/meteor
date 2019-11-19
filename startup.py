from typing import List
from starlette.applications import Starlette
from starlette.responses import UJSONResponse
import uvicorn


class AppStartup(object):
    def __init__(self) -> None:
        self._routes: List = []
        self._app: Starlette = Starlette(debug=False)


@app.route('/')
async def hello(request):
    return UJSONResponse({'hello': 'world'})

if __name__ == '__main__':
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=8000,
                workers=4,
                http="httptools",
                loop="uvloop")
