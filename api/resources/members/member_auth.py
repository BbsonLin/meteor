from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route, Mount
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from api.validators.members import MemberLoginValidator
from infrastructures.logging import meteor_logman
from packages.webargs import parse_requests


class MemberLoginAPIResource(HTTPEndpoint):

    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({"path": "Members"})

    @parse_requests(MemberLoginValidator())
    async def post(self, request: Request, reqargs: dict) -> UJSONResponse:
        return UJSONResponse({
            "member_id": "MEM2019112613551501"
        })


member_auth_routes = Mount(
    "/auth", routes=[
        Route("/login", MemberLoginAPIResource)
    ]
)
