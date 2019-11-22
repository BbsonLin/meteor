from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from api.validators.users import CreateUserValidator, EditUserValidator
from infrastructures.logging import console_logger
from packages.webargs import parse_requests


class UsersAPIResource(HTTPEndpoint):

    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({'path': 'Users'})

    @parse_requests(CreateUserValidator())
    async def post(self, request: Request, reqargs: dict) -> UJSONResponse:
        console_logger.info(reqargs)
        return UJSONResponse({
            'data': reqargs
        })


class UserAPIResource(HTTPEndpoint):
    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({
            "user_id": request.path_params["user_id"]
        })

    @parse_requests(EditUserValidator())
    async def patch(self, request: Request, reqargs: dict) -> UJSONResponse:
        return UJSONResponse({
            'data': reqargs,
            "user_id": request.path_params["user_id"]
        })


users_router = Route("/users", UsersAPIResource)
user_router = Route("/users/{user_id}", UserAPIResource)
