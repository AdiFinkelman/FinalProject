from my_parser import Parser
from lexer import Lexer
from interpreter import Interpreter
 
while True:
    line = input(">>> ")
    lexer = Lexer(line)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree: continue
    interpreter = Interpreter()
    value = interpreter.interpret(tree)
    print(value)
    
    if line.strip() == "quit":
        break