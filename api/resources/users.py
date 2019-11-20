from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from infrastructures.logging import console_logger


class UsersResource(HTTPEndpoint):
    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({'path': 'Users'})

    async def post(self, request: Request) -> UJSONResponse:
        json = await request.json()
        return UJSONResponse(json)


class UserResource(HTTPEndpoint):
    async def get(self, request: Request) -> UJSONResponse:
        username = request.path_params["username"]
        return UJSONResponse({
            'path': 'User',
            "username": username
        })


users_router = Route("/users", UsersResource)
user_router = Route("/user/{username}", UserResource)
