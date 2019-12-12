from typing import List, Optional
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from infrastructures.logging import cheetah_logger
from packages.webargs import parse_requests
import json



class MemberGiftsAPIResource(HTTPEndpoint):
   async def get(self, request: Request) -> UJSONResponse:
        return UJSONResponse( {
                                "success": True,
                                "data": [
                                            {
                                                "type": "1", 
                                                "type_name": "加息卷", 
                                                "description":"子帳戶55萬內，30天加息1%", 
                                                "gift_id": "gift_id",
                                                "invitation":{
                                                                "code": "55CC01",
                                                                "url": "https://nextbanktw.sharepoint.com/sites/IT/55CC01"
                                                            }
                                            },
                                            {
                                                "type": "1", 
                                                "type_name": "加息卷", 
                                                "description":"子帳戶60萬內，30天加息2%", 
                                                "gift_id": "gift_id",
                                                "invitation":{
                                                                "code": "60CC02",
                                                                "url": "https://nextbanktw.sharepoint.com/sites/IT/60CC02"
                                                            }
                                            },
                                            {
                                                "type": "1", 
                                                "type_name": "加息卷", 
                                                "description":"子帳戶65萬內，30天加息3%", 
                                                "gift_id": "gift_id",
                                                "invitation":{
                                                                "code": "65CC03",
                                                                "url": "https://nextbanktw.sharepoint.com/sites/IT/65CC03"
                                                            }
                                            },
                                            {
                                                "type": "1", 
                                                "type_name": "加息卷", 
                                                "description":"子帳戶70萬內，30天加息4%", 
                                                "gift_id": "gift_id",
                                                "invitation":{
                                                                "code": "70CC04",
                                                                "url": "https://nextbanktw.sharepoint.com/sites/IT/70CC04"
                                                            }
                                            },
                                            {
                                                "type": "1", 
                                                "type_name": "加息卷", 
                                                "description":"子帳戶75萬內，30天加息5%", 
                                                "gift_id": "gift_id",
                                                "invitation":{
                                                                "code": "75CC05",
                                                                "url": "https://nextbanktw.sharepoint.com/sites/IT/75CC05"
                                                            }
                                            }
                                        ]
                                }
                                
                            )

gifts_router = Route("/members/{member_id}/gifts", MemberGiftsAPIResource)
