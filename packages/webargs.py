import functools
from enum import Enum
from webargs_starlette import use_args, use_annotations


class HttpContentSource(Enum):
    QUERY = "query"
    JSON = "json"
    FORM = "form"
    FILES = "files"
    HEADERS = "headers"


parse_requests = use_args
parse_query = functools.partial(parse_requests, locations=(HttpContentSource.QUERY.value,))
parse_form = functools.partial(parse_requests, locations=(HttpContentSource.FORM.value,))
parse_json = functools.partial(parse_requests, locations=(HttpContentSource.JSON.value,))
parse_files = functools.partial(parse_requests, locations=(HttpContentSource.FILES.value,))
parse_headers = functools.partial(parse_requests, locations=(HttpContentSource.HEADERS.value,))
parse_body = functools.partial(parse_requests, locations=(HttpContentSource.JSON.value,
                                                          HttpContentSource.FORM.value,
                                                          HttpContentSource.QUERY.value,))
