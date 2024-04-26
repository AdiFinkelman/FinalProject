from tokens import Token, TokenType
import re

# Define constants for lexer
WHITESPACE = ' \n\t'
DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Lexer class for tokenizing input text
class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    # Token generator method
    def generate_tokens(self):
        while self.current_char != None:
            # Skip whitespace characters
            while self.current_char in WHITESPACE:
                self.advance()
            # Tokenize numbers or arithmetic operators
            if self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '%':
                self.advance()
                yield Token(TokenType.MODULO)
            # Tokenize numbers or equation operators
            elif self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    yield Token(TokenType.EQUALS)
                else:
                    raise Exception("Invalid character '='")
            elif self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    yield Token(TokenType.NOT_EQUALS)
                else:
                    yield Token(TokenType.NOT)
            elif self.current_char == '>':
                self.advance()
                yield Token(TokenType.GREATER_THAN)
            elif self.current_char == '<':
                self.advance()
                yield Token(TokenType.LESS_THAN)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == '&':
                self.advance()
                yield Token(TokenType.AND)
            elif self.current_char == '|':
                self.advance()
                yield Token(TokenType.OR)
            elif self.current_char == '!':
                self.advance()
                yield Token(TokenType.NOT)
            elif self.current_char in LETTERS:
                # Tokenize keywords or variables
                keyword = self.current_char
                self.advance()
                while self.current_char is not None and self.current_char in LETTERS:
                    keyword += self.current_char
                    self.advance()
                if keyword == "if":
                    yield Token(TokenType.IF)
                elif keyword == "while":
                    yield Token(TokenType.WHILE)
                elif len(keyword) == 1:
                    yield Token(TokenType.VARIABLE, keyword)
                    while self.current_char == ' ':
                        self.advance()
                if self.current_char == '=':
                    # Tokenize assignment or comparison operators
                    self.advance()
                    if self.current_char == '=':
                        self.advance()
                        yield Token(TokenType.EQUALS)
                    else:
                        yield Token(TokenType.ASSIGN)  
            elif self.current_char == ':':
                self.advance()
                yield Token(TokenType.COLON)
            else:
                raise Exception(f"Illegal character: '{self.current_char}'")
    
    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break
        
            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'
        
        if number_str.count('.') > 1:
            raise Exception("Invalid number")
        
        if number_str.startswith('-'):
            if number_str.count('-') > 1:
                raise Exception("Invalid number")
            return Token(TokenType.NUMBER, -float(number_str[1:]))
        if number_str.startswith('+'):
            if number_str.count('+') > 1:
                raise Exception("Invalid number")
            return Token(TokenType.NUMBER, float(number_str[1:]))
        
        return Token(TokenType.NUMBER, float(number_str))