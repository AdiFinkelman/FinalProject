from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
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
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.POWER)
            elif self.current_char == '==':
                self.advance()
                yield Token(TokenType.EQUALS)
            elif self.current_char == '!=':
                self.advance()
                yield Token(TokenType.NOT_EQUALS)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char in LETTERS:
                yield self.generate_word()
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
            
    def generate_word(self):
        word = self.current_char
        self.advance()
        while self.current_char != None and self.current_char in LETTERS:
            word += self.current_char
            self.advance()
        return Token(TokenType.LETTER, word) 
        