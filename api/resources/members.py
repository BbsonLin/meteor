from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from api.validators.members import CreateMemberValidator, EditMemberValidator
from apps.datacontracts.commands import CreateMemberCommand, EditMemberCommand
from apps.datacontracts.results import MemberResult, MemberLoginResult
from apps.services.members import member_service
from infrastructures.logging import console_logger
from packages.webargs import parse_requests


class MembersAPIResource(HTTPEndpoint):

    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({"path": "Members"})

    @parse_requests(CreateMemberValidator())
    async def post(self, request: Request, reqargs: dict) -> UJSONResponse:
        # console_logger.info(reqargs)
        command = CreateMemberCommand(**reqargs)
        # results: MemberResult = member_service.create_member(command)
        return UJSONResponse({
            "data": reqargs
        })


class MemberAPIResource(HTTPEndpoint):
    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({
            "member_id": request.path_params["member_id"]
        })

    @parse_requests(EditMemberValidator())
    async def patch(self, request: Request, reqargs: dict) -> UJSONResponse:
        command = EditMemberCommand(**reqargs)
        return UJSONResponse({
            "data": reqargs,
            "member_id": request.path_params["member_id"]
        })


members_router = Route("/members", MembersAPIResource)
member_router = Route("/members/{member_id}", MemberAPIResource)
