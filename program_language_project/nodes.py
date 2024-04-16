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
class PowNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} ** {self.node_b})"

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