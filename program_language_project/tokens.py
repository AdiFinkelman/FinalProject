from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    NUMBER          = 0
    PLUS            = 1
    MINUS           = 2
    MULTIPLY        = 3
    DIVIDE          = 4
    LPAREN          = 5
    RPAREN          = 6
    LETTER          = 7
    MODULO          = 8
    EQUAL           = 9
    NOT_EQUALS      = 10
    GREATER_THAN    = 11
    LESS_THAN       = 12
    AND             = 13
    OR              = 14
    NOT             = 15
    IF              = 16
    WHILE           = 17
    ASSIGN          = 18
    VARIABLE        = 19
    COLON           = 20

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f": {self.value}" if self.value != None else "")