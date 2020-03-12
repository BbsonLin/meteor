from typing import Dict, Any
from dataclasses import dataclass
from starlette.responses import UJSONResponse
from http import HTTPStatus


@dataclass(frozen=True)
class ErrorRespTranslator(object):
    code: str
    message: str

    def to_response(self, status_code: int = HTTPStatus.OK) -> UJSONResponse:
        return UJSONResponse({
            "success": False,
            "data": {
                "error_code": self.code,
                "error_message": self.message
            }
        }, status_code)
