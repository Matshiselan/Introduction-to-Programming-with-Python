# core/evaluator.py

from core.registry import OPERATORS
from utils.errors import EvaluationError


def evaluate_rpn(rpn_tokens):
    stack = []

    for token in rpn_tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in OPERATORS:
            try:
                b = stack.pop()
                a = stack.pop()
            except IndexError:
                raise EvaluationError("Malformed expression.")

            func = OPERATORS[token][0]
            stack.append(func(a, b))
        else:
            raise EvaluationError(f"Unknown token: {token}")

    if len(stack) != 1:
        raise EvaluationError("Malformed expression.")

    return stack[0]
