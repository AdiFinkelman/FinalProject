from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    NUMBER  = 0
    PLUS    = 1
    MINUS   = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    LETTER = 7
    MODULO = 8
    EQUAL = 9
    NOT_EQUALS = 10
    GREATER_THAN = 11
    LESS_THAN = 12
    GREATER_THAN_OR_EQUAL = 13
    LESS_THAN_OR_EQUAL = 14
    AND = 15
    OR = 16
    NOT = 17
    IF = 18
    ELSE = 19
    WHILE = 20
    FOR = 21 
    ASSIGN = 22
    VARIABLE = 23

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f": {self.value}" if self.value != None else "")