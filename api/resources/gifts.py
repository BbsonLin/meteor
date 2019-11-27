from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
# from api.validators.members import CreateMemberValidator, EditMemberValidator
#from apps.datacontracts.commands import CreateMemberCommand, EditMemberCommand
from infrastructures.logging import console_logger
from packages.webargs import parse_requests
import json



class MemberGiftsAPIResource(HTTPEndpoint):
   async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse( {
                                "success": True,
                                "data": [
                                            {
                                                "type": "Type", 
                                                "type_name": "加息卷", 
                                                "description":"description", 
                                                "gift_id": "gift_id",
                                                "invitation":{
                                                                "code": "XYXYXXX",
                                                                "url": "url"
                                                            }
                                            }
                                        ]
                                }
                                
                            )

gifts_router = Route("/members/{member_id}/gifts", MemberGiftsAPIResource)
