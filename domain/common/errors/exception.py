from .code import DomainErrorCode
from typing import Optional


class DomainException(Exception):
    def __init__(self, error_code: DomainErrorCode, inner: Optional[Exception] = None, stack_trace: Optional[str] = None) -> None:
        self._error_code = error_code.name
        self._error_message = error_code.value
        self._inner = inner
        self._stack_trace = stack_trace

    @property
    def error_code(self) -> str:
        return self._error_code

    @property
    def error_message(self) -> str:
        return self._error_message

    @property
    def inner(self) -> Optional[Exception]:
        return self._inner

    @property
    def stack_trace(self) -> Optional[str]:
        return self._stack_trace

    def __str__(self) -> str:
        return "<source: {src}, code: {code}, message: {message}>".format(src=self.source,
                                                                          code=self.error_code,
                                                                          message=self.error_message)

    def __repr__(self) -> str:
        return "<DomainException:\n\
                code: {code} \n\
                message: {message} \n\
                inner={inner}\n\
                stack_trace={trace}>".format(code=self.error_code,
                                             message=self.error_message,
                                             inner=type(self.inner).__name__ if self.inner else None,
                                             trace=type(self.stack_trace).__name__ if self.inner else None)
 