import operator
import math

OPERATORS = {
    '+': (operator.add, 1),
    '-': (operator.sub, 1),
    '*': (operator.mul, 2),
    '/': (operator.truediv, 2),
    '^': (operator.pow, 3),
}

FUNCTIONS = {
    'sqrt': math.sqrt,
    'cbrt': lambda x: x ** (1/3),
    'log': math.log10,
    'ln': math.log,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
}
