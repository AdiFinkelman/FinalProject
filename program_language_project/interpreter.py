from nodes import *
from result import Result

class Interpreter:
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
    
    def visit_GreaterThanEqualNode(self, node):
        return Result(self.visit(node.node_a).value >= self.visit(node.node_b).value)
    
    def visit_LessThanEqualNode(self, node):
        return Result(self.visit(node.node_a).value <= self.visit(node.node_b).value)
    
    def visit_PlusNode(self, node):
        return Result(self.visit(node.node).value)
    
    def visit_MinusNode(self, node):
        return Result(-self.visit(node.node).value)
    
    def interpret(self, node):
        return self.visit(node)