# functions/arithmetic.py

import operator
from utils.errors import DivisionByZeroError


def add(a: float, b: float) -> float:
    return operator.add(a, b)


def subtract(a: float, b: float) -> float:
    return operator.sub(a, b)


def multiply(a: float, b: float) -> float:
    return operator.mul(a, b)


def divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Division by zero is undefined.")
    return operator.truediv(a, b)


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Modulo by zero is undefined.")
    return operator.mod(a, b)
