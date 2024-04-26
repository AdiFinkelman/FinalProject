import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):
	
	def test_empty(self):
		# Test empty input string
		tokens = list(Lexer("").generate_tokens())
		self.assertEqual(tokens, [])
	
	def test_whitespace(self):
		# Test input string with only whitespace characters
		tokens = list(Lexer(" \t\n  \t\t\n\n").generate_tokens())
		self.assertEqual(tokens, [])

	def test_numbers(self):
		# Test parsing of different number formats
		tokens = list(Lexer("123 123.456 123. .456 .").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.NUMBER, 123.000),
			Token(TokenType.NUMBER, 123.456),
			Token(TokenType.NUMBER, 123.000),
			Token(TokenType.NUMBER, 000.456),
			Token(TokenType.NUMBER, 000.000),
		])
	
	def test_operators(self):
		# Test parsing of arithmetic operators
		tokens = list(Lexer("+-*/").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.PLUS),
			Token(TokenType.MINUS),
			Token(TokenType.MULTIPLY),
			Token(TokenType.DIVIDE),
		])

	def test_parens(self):
		# Test parsing of parentheses
		tokens = list(Lexer("()").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.LPAREN),
			Token(TokenType.RPAREN),
		])
	
	def test_assignment(self):
		# Test parsing of variable assignment
		tokens = list(Lexer("x = 10").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.VARIABLE, 'x'),
			Token(TokenType.ASSIGN),
			Token(TokenType.NUMBER, 10),
		])

	def test_comparison_operators(self):
		# Test parsing of comparison operators
		tokens = list(Lexer("x == y != z > a < b").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.VARIABLE, 'x'),
			Token(TokenType.EQUALS),
			Token(TokenType.VARIABLE, 'y'),
			Token(TokenType.NOT_EQUALS),
			Token(TokenType.VARIABLE, 'z'),
			Token(TokenType.GREATER_THAN),
			Token(TokenType.VARIABLE, 'a'),
			Token(TokenType.LESS_THAN),
			Token(TokenType.VARIABLE, 'b'),
		])

	def test_logical_operators(self):
		# Test parsing of logical operators
		tokens = list(Lexer("x & y | !z").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.VARIABLE, 'x'),
			Token(TokenType.AND),
			Token(TokenType.VARIABLE, 'y'),
			Token(TokenType.OR),
			Token(TokenType.NOT),
			Token(TokenType.VARIABLE, 'z'),
		])

	def test_keywords(self):
		# Test parsing of keywords
		tokens = list(Lexer("if (x == 10) { y = 20 }").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.IF),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'x'),
			Token(TokenType.EQUALS),
			Token(TokenType.NUMBER, 10),
			Token(TokenType.RPAREN),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'y'),
			Token(TokenType.ASSIGN),
			Token(TokenType.NUMBER, 20),
			Token(TokenType.RPAREN),
		])
	
	def test_all(self):
		# Test parsing of a complex expression
		tokens = list(Lexer("27 + (43 / 36 - 48) * 51").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.PLUS),
			Token(TokenType.LPAREN),
			Token(TokenType.NUMBER, 43),
			Token(TokenType.DIVIDE),
			Token(TokenType.NUMBER, 36),
			Token(TokenType.MINUS),
			Token(TokenType.NUMBER, 48),
			Token(TokenType.RPAREN),
			Token(TokenType.MULTIPLY),
			Token(TokenType.NUMBER, 51),
		])
