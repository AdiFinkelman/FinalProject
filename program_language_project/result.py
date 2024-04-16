from dataclasses import dataclass

@dataclass
class Result:
    value: float

    def __repr__(self):
        return f"{self.value}"