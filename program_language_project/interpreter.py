from nodes import *
from result import Result

class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}" # AddNode -> visit_AddNode
        method = getattr(self, method_name)
        return method(node)
    
    def visit_NumberNode(self, node):
        return Result(node.value)
    
    def visit_AddNode(self, node):
        return Result(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_SubNode(self, node):
        return Result(self.visit(node.node_a).value - self.visit(node.node_b).value)
    
    def visit_MulNode(self, node):
        return Result(self.visit(node.node_a).value * self.visit(node.node_b).value)
    
    def visit_DivNode(self, node):
        try:
            return Result(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")
    
    def visit_ModNode(self, node):
        return Result(self.visit(node.node_a).value % self.visit(node.node_b).value)
    
    def visit_EqualsNode(self, node):
        return Result(self.visit(node.node_a).value == self.visit(node.node_b).value)

    def visit_Not_EqualsNode(self, node):
        return Result(self.visit(node.node_a).value != self.visit(node.node_b).value)
    
    def visit_GreaterThanNode(self, node):
        return Result(self.visit(node.node_a).value > self.visit(node.node_b).value)
    
    def visit_LessThanNode(self, node):
        return Result(self.visit(node.node_a).value < self.visit(node.node_b).value)
    
    def visit_PlusNode(self, node):
        return Result(self.visit(node.node).value)
    
    def visit_MinusNode(self, node):
        return Result(-self.visit(node.node).value)
    
    def visit_VariableNode(self, node):
        variable_name = node.name
        if variable_name not in self.variables:
            raise Exception(f"Variable '{variable_name}' not defined")
        return Result(self.variables[variable_name])

    def visit_AssignNode(self, node):
        variable_name = node.variable.name
        value = self.visit(node.value).value
        self.variables[variable_name] = value
        return Result(value)
    
    def visit_IfNode(self, node):
        if self.visit(node.condition).value:
            return self.visit(node.body)
        return Result("None")
    
    def visit_WhileNode(self, node):
        while self.visit(node.condition_node).value:
            self.visit(node.node)
        return Result(None)
    
    def visit_AndNode(self, node):
        return Result(self.visit(node.node_a).value and self.visit(node.node_b).value)
    
    def visit_OrNode(self, node):
        return Result(self.visit(node.node_a).value or self.visit(node.node_b).value)
    
    def visit_NotNode(self, node):
        return Result(not self.visit(node.node).value)

    def interpret(self, node):
        return self.visit(node)