from rest_framework.response import Response
from rest_framework.views import exception_handler

from core_temp.enums.error_enum import ErrorEnum


def custom_exception_handler(exc: Exception, context: dict) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error
    }
    response = exception_handler(exc, context)
    exc_class = exc.__class__.__name__
    if exc_class in handlers:
        function = handlers[exc_class]
        return function(exc, context)
    return response


def _jwt_validate_error(exc: Exception, context: dict) -> Response:
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)