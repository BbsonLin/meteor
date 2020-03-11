import sys
import logging
from domain.common import DomainException
from starlette.requests import Request
from starlette_context import context
from starlette.responses import Response, UJSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, ASGIApp
from starlette.exceptions import HTTPException
from .translator import ErrorRespTranslator
from infrastructures.logging import cheetah_logger
from http import HTTPStatus
import traceback


class ExceptHandlerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            headers = request.headers.values()
            # FIXME 該段 await 會有問題, 需把 logging 的部分移動到每一個 HTTP Requests Verb 方法中或包一層 Decorator
            req_content = await request.json()
            cheetah_logger.info("Request content below shown \n - HEADER : %s \n - BODY : %s", headers, req_content)
            response = await call_next(request)
            cheetah_logger.info("Response content : %s", await response.body_iterator())
            return response
        except DomainException as dex:
            translator = ErrorRespTranslator(dex.error_code, dex.error_message)
            cheetah_logger.warning(traceback.format_exc())
            return translator.to_response()
        except Exception as ex:
            translator = ErrorRespTranslator("INTERNAL_SERVER_ERROR", "Internal Server Error")
            cheetah_logger.error(traceback.format_exc())
            return translator.to_response(HTTPStatus.INTERNAL_SERVER_ERROR)
