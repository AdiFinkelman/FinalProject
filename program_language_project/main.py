from my_parser import Parser
from lexer import Lexer
from interpreter import Interpreter
 
interpreter = Interpreter()

while True:
    try:
        line = input(">>> ")

        if line.strip() == "exit":
            break

        lexer = Lexer(line)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        value = interpreter.interpret(tree)
        print(value)
        
    except Exception as e:
        print("Error:", e)