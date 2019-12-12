from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from api.validators.auth import MemberLoginValidator
from infrastructures.logging import cheetah_logger
from packages.webargs import parse_requests


class MemberLoginAPIResource(HTTPEndpoint):

    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({"path": "Members"})

    @parse_requests(MemberLoginValidator())
    async def post(self, request: Request, reqargs: dict) -> UJSONResponse:
        return UJSONResponse({
            "member_id": "MEM2019112613551501"
        })


login_router = Route("/login", MemberLoginAPIResource)
