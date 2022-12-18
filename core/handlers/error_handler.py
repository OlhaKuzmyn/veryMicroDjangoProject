from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.enums.error_enum import ErrorEnum


def custom_exception_handler(exc: Exception, context: dict) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error,
        'ScheduleException': _schedule_validate_error,
        'CharacterAlreadyAddedException': _char_added_validate_error,
        'CampaignOverException': _campaign_over_validate_error,
    }
    response = exception_handler(exc, context)
    exc_class = exc.__class__.__name__
    if exc_class in handlers:
        function = handlers[exc_class]
        return function(exc, context)
    return response


def _jwt_validate_error(exc: Exception, context: dict) -> Response:
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)


def _schedule_validate_error(exc: Exception, context: dict) -> Response:
    return Response(ErrorEnum.SCHEDULE.msg, ErrorEnum.SCHEDULE.code)


def _char_added_validate_error(exc: Exception, context: dict) -> Response:
    return Response(ErrorEnum.CHAR_ADDED.msg, ErrorEnum.CHAR_ADDED.code)


def _campaign_over_validate_error(exc: Exception, context: dict) -> Response:
    return Response(ErrorEnum.CAMPAIGN_OVER.msg, ErrorEnum.CAMPAIGN_OVER.code)
