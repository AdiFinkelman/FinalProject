from dataclasses import dataclass

@dataclass
class Result:
    value: float

    def __repr__(self):
        if self.value != None:
            return f"{self.value}"