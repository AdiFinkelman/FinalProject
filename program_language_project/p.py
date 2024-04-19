import re

class SimpleLangInterpreter:
    def __init__(self):
        self.variables = {}

    def run(self):
        while True:
            line = input("<<< ")
            if line.strip() == "quit":
                break
            try:
                result = self.evaluate(line)
                if result is not None:
                    print(result)
            except ValueError as e:
                print(f"Error: {e}")

    def evaluate(self, statement):
        if ">" in statement or "<" in statement or "==" in statement:
            return self.evaluate_boolean_expression(statement)
        elif statement.startswith("read"):
            self.read_command(statement)
        elif "=" in statement:
            try:
                self.assign_variable(statement)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            try:
                return self.evaluate_expression(statement)
            except ValueError as e:
                print(f"Error: {e}")


    def assign_variable(self, assignment):
        parts = re.split(r'\s*=\s*', assignment)
        variable = parts[0].strip()
        if len(variable) != 2 or not variable[0].isalpha():
            raise ValueError("Variable name must be exactly two letters and start with a letter")
        expr = parts[1].strip()
        value = self.evaluate_expression(expr)
        self.variables[variable] = value

    def evaluate_expression(self, expr):
        try:
            return eval(expr, {}, self.variables)
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {e}")

    def evaluate_boolean_expression(self, expr):
        try:
            return eval(expr, {}, self.variables)
        except Exception as e:
            raise ValueError(f"Error evaluating boolean expression: {e}")

    def read_command(self, statement):
        args = re.findall(r'\b(\w+)\s*=\s*([^,]+)', statement[len("read"):])
        for var_name, expr in args:
            var_name = var_name.strip()
            if len(var_name) != 2 or not var_name[0].isalpha():
                print(f"Error: Variable name '{var_name}' must be exactly two letters and start with a letter")
                continue
            try:
                value = self.evaluate_expression(expr.strip())
                self.variables[var_name] = value
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    interpreter = SimpleLangInterpreter()
    interpreter.run()