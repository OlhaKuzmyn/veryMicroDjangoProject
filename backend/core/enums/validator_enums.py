from enum import Enum


class ValidatorEnum(Enum):
    BEYOND_URL = (
        r'^(?:https?:\/\/)?(?:www\.)?(dndbeyond\.com\/(characters\/([0-9]{8})))$',
        'invalid url for DnD Beyond character sheet'
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
