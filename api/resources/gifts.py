from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from infrastructures.logging import console_logger
from packages.webargs import parse_requests
from apps.datacontracts.commands import GetGiftByIdCommand
from apps.services import gift_service
from apps.datacontracts.results import GiftResult
from api.responses.gifts import GiftResponse


class MemberGiftsAPIResource(HTTPEndpoint):
   async def get(self, request: Request) -> UJSONResponse:
       command = GetGiftByIdCommand(**request.path_params)
       result: GiftResult = gift_service.get(command)
       resp = GiftResponse().dump(result)
       return UJSONResponse(resp)

gifts_router = Route("/members/{member_id}/gifts", MemberGiftsAPIResource)
