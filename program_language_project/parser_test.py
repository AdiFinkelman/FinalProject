import unittest
from tokens import Token, TokenType
from my_parser import Parser
from nodes import *

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 51.2)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(51.2))

    def test_single_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(27), NumberNode(14)))
        
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, SubNode(NumberNode(27), NumberNode(14)))
            
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, MulNode(NumberNode(27), NumberNode(14)))
            
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, DivNode(NumberNode(27), NumberNode(14)))

    def test_full_expression(self):
        tokens = [
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
        ]

        node = Parser(tokens).parse()
        expected_node = AddNode(
            NumberNode(27),
            MulNode(
                SubNode(
                    DivNode(
                        NumberNode(43),
                        NumberNode(36)
                    ),
                    NumberNode(48)
                ),
                NumberNode(51)
            )
        )
        self.assertEqual(node, expected_node)

    def test_comparison_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.GREATER_THAN),
            Token(TokenType.NUMBER, 5),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, GreaterThanNode(NumberNode(10), NumberNode(5)))

        tokens = [
            Token(TokenType.NUMBER, 5),
            Token(TokenType.LESS_THAN),
            Token(TokenType.NUMBER, 10),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, LessThanNode(NumberNode(5), NumberNode(10)))

        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.EQUALS),
            Token(TokenType.NUMBER, 10),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, EqualsNode(NumberNode(10), NumberNode(10)))

        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.NOT_EQUALS),
            Token(TokenType.NUMBER, 5),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, Not_EqualsNode(NumberNode(10), NumberNode(5)))

    def test_logical_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 1),
            Token(TokenType.AND),
            Token(TokenType.NUMBER, 0),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AndNode(NumberNode(1), NumberNode(0)))

        tokens = [
            Token(TokenType.NUMBER, 1),
            Token(TokenType.OR),
            Token(TokenType.NUMBER, 0),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, OrNode(NumberNode(1), NumberNode(0)))

        tokens = [
            Token(TokenType.NOT),
            Token(TokenType.NUMBER, 1),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, NotNode(NumberNode(1)))

    def test_assignment(self):
        tokens = [
            Token(TokenType.VARIABLE, 'x'),
            Token(TokenType.ASSIGN),
            Token(TokenType.NUMBER, 10),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AssignNode(VariableNode('x'), NumberNode(10)))

    def test_conditional_statement(self):
        tokens = [
            Token(TokenType.IF),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 10),
            Token(TokenType.GREATER_THAN),
            Token(TokenType.NUMBER, 5),
            Token(TokenType.RPAREN),
            Token(TokenType.COLON),
            Token(TokenType.NUMBER, 20),
        ]

        node = Parser(tokens).parse()
        expected_node = IfNode(
            GreaterThanNode(NumberNode(10), NumberNode(5)),
            NumberNode(20)
        )
        self.assertEqual(node, expected_node)
