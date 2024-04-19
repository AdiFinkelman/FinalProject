from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"
    
@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} + {self.node_b})"

@dataclass
class SubNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} - {self.node_b})"
    
@dataclass
class MulNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} * {self.node_b})"

@dataclass
class DivNode:    
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"
    
@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"
	
@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"
     
@dataclass
class ModNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} % {self.node_b})"

@dataclass
class EqualsNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} == {self.node_b})"

@dataclass
class Not_EqualsNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} != {self.node_b})"
    
@dataclass
class GreaterThanNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} > {self.node_b})"
    
@dataclass
class LessThanNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} < {self.node_b})"
    
@dataclass
class GreaterThanEqualNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} >= {self.node_b})"
    
@dataclass
class LessThanEqualNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} <= {self.node_b})"
    
@dataclass
class AndNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} && {self.node_b})"
    
@dataclass
class OrNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} || {self.node_b})"

@dataclass
class NotNode:
    node: any

    def __repr__(self):
        return f"(!{self.node})"
    
@dataclass
class IfNode:
    condition: any
    body: any

    def __repr__(self):
        return f"(if {self.condition} {self.body})"
    
@dataclass
class ElseNode:
    body: any

    def __repr__(self):
        return f"(else {self.body})"
    
@dataclass
class WhileNode:
    condition: any
    body: any

    def __repr__(self):
        return f"(while {self.condition} {self.body})"
    
@dataclass
class ForNode:
    condition: any
    body: any

    def __repr__(self):
        return f"(for {self.condition} {self.body})"
    
@dataclass
class AssignNode:
    variable: str
    value: float

    def __repr__(self):
        return f"({self.variable} = {self.value})"
    
@dataclass
class VariableNode:
    name: str
    value: float

    def __repr__(self):
        return f"{self.value}"