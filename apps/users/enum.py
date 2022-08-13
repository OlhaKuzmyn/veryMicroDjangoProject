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
        r'^.*\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*.*$',
        [
            'telegram username must begin with @'
        ]
    )
    DISCORD = (
        r'^.{3,32}#[0-9]{4}$',
        [
            'discord username must have # in'
        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
