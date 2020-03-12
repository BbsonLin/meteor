import sys
import logging
from domain.common import DomainException
from starlette.requests import Request
from starlette_context import context
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, ASGIApp
from starlette.exceptions import HTTPException
from .translator import ErrorRespTranslator
from infrastructures.logging import cheetah_logger
from http import HTTPStatus
import traceback


# class ExceptHandlerMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app: ASGIApp):
#         self._app = app

#     async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
#         try:
#             headers = Headers(scope=scope)
#             request = Request(scope, receive=receive)
#             req_content = await request.json()
#             cheetah_logger.info("Request content below shown \n - HEADER : %s \n - BODY : %s", headers, req_content)
#             await self._app(scope, receive, send)
#             cheetah_logger.info("Response content : %s", response.status_code)
#             await response(scope, receive, send)
#         except DomainException as dex:
#             translator = ErrorRespTranslator(dex.error_code, dex.error_message)
#             cheetah_logger.warning(traceback.format_exc())
#             response = translator.to_response()
#             await response(scope, receive, send)
#         except Exception as ex:
#             translator = ErrorRespTranslator("INTERNAL_SERVER_ERROR", "Internal Server Error")
#             cheetah_logger.error(traceback.format_exc())
#             response = translator.to_response(HTTPStatus.INTERNAL_SERVER_ERROR)
#             await response(scope, receive, send)

class ExceptHandlerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        try:
            headers = request.headers.values()
            # NOTE: 根據網友的 PR 先手動修改 Request 的 receive 方法 https://github.com/encode/starlette/pull/848
            req_content = await request.json()
            cheetah_logger.info("Request content below shown \n - HEADER : %s \n - BODY : %s", headers, req_content)
            response = await call_next(request)
            cheetah_logger.info("Response content : %s", response.status_code)
            return response
        except DomainException as dex:
            translator = ErrorRespTranslator(dex.error_code, dex.error_message)
            cheetah_logger.warning(traceback.format_exc())
            return translator.to_response()
        except Exception as ex:
            translator = ErrorRespTranslator("INTERNAL_SERVER_ERROR", "Internal Server Error")
            cheetah_logger.error(traceback.format_exc())
            return translator.to_response(HTTPStatus.INTERNAL_SERVER_ERROR)
