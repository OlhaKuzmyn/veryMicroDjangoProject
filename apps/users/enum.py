from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,20}$',
        [
            'password must contain 1 number(0 - 9)',
            'password must contain 1 uppercase letters',
            'password must contain 1 lowercase letters',
            'password must contain 1 non - alpha numeric number',
            'password is 8 - 20 characters with no space'
        ]
    )
    NAME = (
        r'^[a-zA-Z]{2,100}$',
        'only letters min 2 max 100 characters'
    )
    TELEGRAM = (
        r'/^[@](?:(?=[a-zA-Z\d]{1,20})[A-Za-z]+\d*)$/i',
        [
            'telegram username must begin with @'
        ]
    )
    DISCORD = (
        r'/[\p{L}\d\s#]/u',
        [
            'discord username must begin with #'
        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg