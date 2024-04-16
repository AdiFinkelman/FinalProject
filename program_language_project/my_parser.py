from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
    
    def raise_error(self):
        raise Exception("Invalid syntax")
    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    
    def parse(self):
        if self.current_token == None:
            return None
        
        result = self.expr() 
        if self.current_token != None:
            self.raise_error()
        
        return result
    
    def expr(self):
        result = self.term()
        
        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.EQUAL, TokenType.NOT_EQUALS, TokenType.GREATER_THAN, 
                                                                         TokenType.LESS_THAN, TokenType.GREATER_THAN_OR_EQUAL, TokenType.LESS_THAN_OR_EQUAL):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubNode(result, self.term())
            elif self.current_token.type == TokenType.EQUAL:
                self.advance()
                result = EqualsNode(result, self.term())
            elif self.current_token.type == TokenType.NOT_EQUALS:
                self.advance()
                result = Not_EqualsNode(result, self.term())
            elif self.current_token.type == TokenType.GREATER_THAN:
                self.advance()
                result = GreaterThanNode(result, self.term())
            elif self.current_token.type == TokenType.LESS_THAN:
                self.advance()
                result = LessThanNode(result, self.term())
            elif self.current_token.type == TokenType.GREATER_THAN_OR_EQUAL:
                self.advance()
                result = GreaterThanEqualNode(result, self.term())
            elif self.current_token.type == TokenType.LESS_THAN_OR_EQUAL:
                self.advance()
                result = LessThanEqualNode(result, self.term())
        
        return result
    
    def term(self):
        result = self.factor()
        
        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MulNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivNode(result, self.factor())
            elif self.current_token.type == TokenType.MODULO:
                self.advance()
                result = ModNode(result, self.factor())
        
        return result
    
    
    def factor(self):
        token = self.current_token
        
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()
            
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            
            self.advance()
            return result
        
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())
        
        self.raise_error()