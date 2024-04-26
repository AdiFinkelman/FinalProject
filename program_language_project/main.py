from my_parser import Parser
from lexer import Lexer
from interpreter import Interpreter
 
interpreter = Interpreter()

while True:
    try:
        line = input(">>> ")

        # Check if the user wants to exit
        if line.strip() == "exit":
            break

        # Tokenize the input line
        lexer = Lexer(line)
        tokens = lexer.generate_tokens()

        # Parse the tokens into an abstract syntax tree (AST)
        parser = Parser(tokens)
        tree = parser.parse()
        
        # If the tree is empty, continue to the next iteration
        if not tree: continue

        # Interpret the AST
        value = interpreter.interpret(tree)
        print(value)
        
    except Exception as e:
        print("Error:", e)