from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = ({'details': 'Invalid or expired token'}, status.HTTP_403_FORBIDDEN)
    SCHEDULE = ({'details': 'Game should be scheduled the same day or later than campaign starts'}, status.HTTP_400_BAD_REQUEST)
    CHAR_ADDED = ({'details': 'Character already added'}, status.HTTP_400_BAD_REQUEST)
    CAMPAIGN_OVER = ({'details': 'Selected campaign is over, choose another campaign'}, status.HTTP_400_BAD_REQUEST)

    def __init__(self, msg, code=status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.code = code
        