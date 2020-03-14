from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route, Mount
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from api.validators.members import CreateMemberValidator, EditMemberValidator
from api.responses.members import MemberProfileResp
from apps.datacontracts.commands.members import CreateMemberCmd, EditMemberCmd
from apps.datacontracts.commands.members import GetMemberByIdCmd
from apps.datacontracts.results.members import MemberProfileRst, MemberLoginRst
from apps.services.members import member_profile_service
from infrastructures.logging import meteor_logman
from packages.webargs import parse_requests


class MembersAPIResource(HTTPEndpoint):

    async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse({"path": "Members"})

    @parse_requests(CreateMemberValidator())
    async def post(self, request: Request, reqargs: dict) -> UJSONResponse:
        # meteor_logman.info(reqargs)
        command = CreateMemberCmd(**reqargs)
        result: MemberProfileRst = member_profile_service.create(command)
        resp = MemberProfileResp().dump(result)
        return UJSONResponse({
            "success": True,
            "data": resp
        })


class MemberAPIResource(HTTPEndpoint):
    async def get(self, request: Request) -> UJSONResponse:
        command = GetMemberByIdCmd(**request.path_params)
        result: MemberProfileRst = member_profile_service.get(command)
        resp = MemberProfileResp().dump(result)
        return UJSONResponse(resp)

    @parse_requests(EditMemberValidator())
    async def patch(self, request: Request, reqargs: dict) -> UJSONResponse:
        command = EditMemberCmd(**reqargs)
        return UJSONResponse({
            "data": reqargs,
            "member_id": request.path_params["member_id"]
        })


members_profile_routes = Mount(
    "/members", routes=[
        Route("/", MembersAPIResource),
        Route("/{member_id}", MemberAPIResource),
    ]
)
