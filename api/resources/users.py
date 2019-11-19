from typing import List
from starlette.routing import Route
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from infrastructures.logging import console_logger


class UsersResource(HTTPEndpoint):
    def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({'hello': 'world'})

    def post(self, request: Request) -> UJSONResponse:
        console_logger.debug(request.json)
        return UJSONResponse({'hello': 'world'})


class UserResource(HTTPEndpoint):
    def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({'hello': 'world'})

    def post(self, request: Request) -> UJSONResponse:
        console_logger.debug(request.json)
        return UJSONResponse({'hello': 'world'})


routes = [
    Route("/users", UsersResource),
    Route("/user/{id}", UserResource)
]
