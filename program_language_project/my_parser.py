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
        
        result = self.exp() 
        if self.current_token != None:
            self.raise_error()
        
        return result 
    
    def exp(self):
        result = self.stmt()
        
        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.EQUALS, TokenType.NOT_EQUALS, 
                                                                         TokenType.GREATER_THAN, TokenType.LESS_THAN, TokenType.ASSIGN):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.stmt())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubNode(result, self.stmt())
            elif self.current_token.type == TokenType.EQUALS:
                self.advance()
                result = EqualsNode(result, self.stmt())
            elif self.current_token.type == TokenType.NOT_EQUALS:
                self.advance()
                result = Not_EqualsNode(result, self.stmt())
            elif self.current_token.type == TokenType.GREATER_THAN:
                self.advance()
                result = GreaterThanNode(result, self.stmt())
            elif self.current_token.type == TokenType.LESS_THAN:
                self.advance()
                result = LessThanNode(result, self.stmt())
            elif self.current_token.type == TokenType.ASSIGN:
                self.advance()
                result = AssignNode(result, self.exp())
        
        return result
    
    def stmt(self):
        result = self.factor()
        
        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO, 
                                                                         TokenType.AND, TokenType.OR):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MulNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivNode(result, self.factor())
            elif self.current_token.type == TokenType.MODULO:
                self.advance()
                result = ModNode(result, self.factor())
            elif self.current_token.type == TokenType.AND:
                self.advance()
                result = AndNode(result, self.factor())
            elif self.current_token.type == TokenType.OR:
                self.advance()
                result = OrNode(result, self.factor())
            
        return result
    
    def factor(self):
        token = self.current_token
        
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.exp()
            
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
        elif token.type == TokenType.NOT:
            self.advance()
            return NotNode(self.factor())
        elif token.type == TokenType.IF:
            return condition_stmt(self, token)
        elif token.type == TokenType.VARIABLE:
            self.advance()
            return VariableNode(token.value, token.value) 
        
        self.raise_error()


def condition_stmt(self, token):
    if token.type == TokenType.IF:
            self.advance()
            condition = self.exp()  # Parse the conditional expression
            if self.current_token.type != TokenType.COLON:
                self.raise_error()
            self.advance()
            if_body = self.exp()  # Parse the body of the IF statement
            
            return IfNode(condition, if_body)
