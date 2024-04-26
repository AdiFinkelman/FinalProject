# Simple Python Interpreter

This project is a simple interpreter implemented in Python. It can parse and evaluate basic arithmetic expressions, as well as handle conditional statements (if) and loops (while).

## Features

- Parses and evaluates arithmetic expressions involving addition (+), subtraction (-), multiplication (*), division (/), and modulo (%).
- Supports comparison operators (==, !=, >, <) for conditional expressions.
- Handles logical operators (&, |) for logical expressions.
- Implements unary operators (+, -, !).
- Includes support for variables, if statements, and while loops.

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/AdiFinkelman/Programming-Language-Interpreter.git
```

2. Navigate to the project directory:
```bash
   cd .\Programming-Language-Interpreter\program_language_project\
```

3. Run the interpreter:
```css
   python main.py
```

## Usage

Once the interpreter is running, you can enter expressions at the prompt and get the evaluated result. For example:
```python
>>> 3+4
7.0
>>> a = 7+8
15.0
>>> b = (2+3)*3
15.0
>>> b = b + 1
16.0
>>> c = ((a+b)-15)*2
32.0
>>> if (c > a+b) : d = 1
1.0
>>> d
1.0
>>> if (c > a+b) : if c == 32 : if d != 2 : e = 5   
5.0
>>> e
5.0
>>> while e != 1 : e = e - 1
e = 5.0
e = 4.0
e = 3.0
e = 2.0
1.0
>>> e
1.0
```

To exit the interpreter, type "exit" at the prompt.

## Syntax

The interpreter follows a basic syntax for expressions, statements, and control structures:

- Expressions (<exp>) can be arithmetic expressions, conditional expressions, or logical expressions.
- Statements (<stmt>) are composed of factors and operators.
- Factors (<factor>) can be numbers, variables, or complex expressions enclosed in parentheses.
- Unary operators (<unary_op>) include positive (+), negative (-), and logical NOT (!).
- If statements (<if_stmt>) follow the syntax: "if <condition> : <body>"
- While loops (<while_stmt>) follow the syntax: "while <condition> : <body>"
- Variables (<variable>) are represented by alphabetic characters (case-insensitive) or underscores.

### BNF
![image](https://github.com/AdiFinkelman/Programming-Language-Interpreter/assets/126038641/1d443c12-28e4-42a2-a775-6076c8c3d3f6)

## License

This project is licensed under the MIT License.

## Acknowledgements

- This interpreter is inspired by various resources and tutorials on parsing and interpreting.
- Special thanks to [DEV.to](https://dev.to/codingwithadam/introduction-to-lexers-parsers-and-interpreters-with-chevrotain-5c7b) for their guidance and teaching the interpreter architectural.
  

