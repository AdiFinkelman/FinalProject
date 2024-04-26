import unittest
from nodes import *
from interpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        # Test visiting a NumberNode
        result = Interpreter().visit(NumberNode(51.2))
        self.assertEqual(result.value, 51.2)

    def test_single_operations(self):
        # Test addition operation
        result = Interpreter().visit(AddNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(result.value, 41)

        # Test subtraction operation
        result = Interpreter().visit(SubNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(result.value, 13)

        # Test multiplication operation
        result = Interpreter().visit(MulNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(result.value, 378)

        # Test division by zero
        result = Interpreter().visit(DivNode(NumberNode(27), NumberNode(14)))
        self.assertAlmostEqual(result.value, 1.92857, 5)

        with self.assertRaises(Exception):
            Interpreter().visit(DivNode(NumberNode(27), NumberNode(0)))

    def test_full_expression(self):
        # Test visiting a complex expression tree
        tree = AddNode(
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

        result = Interpreter().visit(tree)
        self.assertAlmostEqual(result.value, -2360.08, 2)

    def test_assignment(self):
        # Test variable assignment
        interpreter = Interpreter()
        assignment_node = AssignNode(VariableNode('x', 0), NumberNode(10))

        # Interpret the assignment
        result = interpreter.visit(assignment_node)

        # Check if the variable was correctly assigned
        self.assertEqual(interpreter.variables['x'], 10)
        self.assertEqual(result.value, 10)

    def test_variable_access(self):
        interpreter = Interpreter()
        interpreter.variables['x'] = 20
        variable_node = VariableNode('x', 0)

        # Interpret the variable access
        result = interpreter.visit(variable_node)

        # Check if the correct value was retrieved
        self.assertEqual(result.value, 20)

    def test_conditional_statement(self):
        # Test accessing a variable
        interpreter = Interpreter()
        conditional_node = IfNode(EqualsNode(NumberNode(5), NumberNode(5)), NumberNode(10))

        # Interpret the conditional statement
        result = interpreter.visit(conditional_node)

        # Check if the correct branch was executed
        self.assertEqual(result.value, 10)

    def test_loop_statement(self):
        # Test interpreting a conditional statement
        interpreter = Interpreter()
        interpreter.variables['x'] = 3
        loop_node = WhileNode(GreaterThanNode(VariableNode('x', 0), NumberNode(0)),
                              AssignNode(VariableNode('x', 0), SubNode(VariableNode('x', 0), NumberNode(1))))

        # Interpret the loop statement
        result = interpreter.visit(loop_node)

        # Check if the loop executed correctly
        self.assertEqual(interpreter.variables['x'], 0)
