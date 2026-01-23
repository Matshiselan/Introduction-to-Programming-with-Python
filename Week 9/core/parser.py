# core/parser.py

# core/parser.py

from core.registry import OPERATORS, FUNCTIONS
from utils.errors import ParseError

def tokenize(expr: str):
    tokens = []
    number = ""
    func = ""
    expr = expr.replace(" ", "")
    i = 0
    while i < len(expr):
        char = expr[i]
        if char.isdigit() or char == ".":
            number += char
            i += 1
        elif char.isalpha():
            func += char
            i += 1
            # Check if next char is not alpha (end of function name)
            if i == len(expr) or not expr[i].isalpha():
                if func in FUNCTIONS:
                    tokens.append(func)
                    func = ""
                else:
                    raise ParseError(f"Unknown function: {func}")
        elif char in OPERATORS:
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(char)
            i += 1
        elif char == '(':  # Support for parentheses (optional, for future RPN)
            if func:
                tokens.append(func)
                func = ""
            tokens.append(char)
            i += 1
        elif char == ')':
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(char)
            i += 1
        else:
            raise ParseError(f"Unknown character: {char}")

    if number:
        tokens.append(float(number))
    if func:
        if func in FUNCTIONS:
            tokens.append(func)
        else:
            raise ParseError(f"Unknown function: {func}")

    return tokens


def to_rpn(tokens):
    output = []
    operators = []

    if not tokens:
        return []

def tokenize(expr: str):
    tokens = []
    number = ""
    func = ""
    expr = expr.replace(" ", "")
    i = 0
    while i < len(expr):
        char = expr[i]
        if char.isdigit() or char == ".":
            number += char
            i += 1
        elif char.isalpha():
            func += char
            i += 1
            # Check if next char is not alpha (end of function name)
            if i == len(expr) or not expr[i].isalpha():
                if func in FUNCTIONS:
                    tokens.append(func)
                    func = ""
                else:
                    raise ParseError(f"Unknown function: {func}")
        elif char in OPERATORS:
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(char)
            i += 1
        elif char == '(':  # Support for parentheses (optional, for future RPN)
            if func:
                tokens.append(func)
                func = ""
            tokens.append(char)
            i += 1
        elif char == ')':
            if number:
                tokens.append(float(number))
                number = ""
            tokens.append(char)
            i += 1
        else:
            raise ParseError(f"Unknown character: {char}")

    if number:
        tokens.append(float(number))
    if func:
        if func in FUNCTIONS:
            tokens.append(func)
        else:
            raise ParseError(f"Unknown function: {func}")

    return tokens
    for token in tokens:
        if isinstance(token, float):
            output.append(token)
        elif token in OPERATORS:
            while (
                operators
                and operators[-1] in OPERATORS
                and OPERATORS[operators[-1]][1] >= OPERATORS[token][1]
            ):
                output.append(operators.pop())
            operators.append(token)
        else:
            raise ParseError(f"Invalid token: {token}")

    while operators:
        output.append(operators.pop())

    return output
