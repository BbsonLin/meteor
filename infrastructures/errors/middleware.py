import sys
from domain.common import DomainException
from starlette.responses import Response, UJSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, ASGIApp
from starlette.exceptions import HTTPException
from .translator import ErrorRespTranslator
from http import HTTPStatus
import traceback


class ExceptHandlerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request, call_next) -> Response:
        try:
            response = await call_next(request)
            return response
        except DomainException as dex:
            translator = ErrorRespTranslator(dex.error_code, dex.error_message)
            return translator.to_response()
        except Exception as ex:
            translator = ErrorRespTranslator("INTERNAL_SERVER_ERROR", "Internal Server Error")
            return translator.to_response(HTTPStatus.INTERNAL_SERVER_ERROR)

