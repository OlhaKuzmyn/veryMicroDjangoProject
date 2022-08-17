from enum import Enum


class ValidatorEnum(Enum):
    TITLE = (
        r'^(\w+)([\W+^\s]){2,200}$',
        "Any letter, symbol, number min 2 max 200"
    )
    RACE = (
        r'^[a-zA-Z]{2,100}$',
        'only letters min 2 max 100 characters'
    )
    BEYOND_URL = (
        r'^(?:https?:\/\/)?(?:www\.)?(dndbeyond\.com\/(characters\/([0-9]{8})))$',
        'invalid url for DnD Beyond character sheet'
    )
    DESCRIPTION = (
        r'^(\w+)([\W+^\s]){10,3000}$',
        "Any letter, symbol, number min 10 max 3000"
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
