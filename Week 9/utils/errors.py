# utils/errors.py

class CalculatorError(Exception):
    """Base class for all calculator-related errors."""
    pass


class ParseError(CalculatorError):
    """Raised when an expression cannot be parsed."""
    pass


class EvaluationError(CalculatorError):
    """Raised when evaluation of an expression fails."""
    pass


class DivisionByZeroError(EvaluationError):
    """Raised when division by zero occurs."""
    pass


class DomainError(EvaluationError):
    """Raised when a mathematical domain error occurs (e.g., sqrt(-1))."""
    pass


class FunctionNotFoundError(EvaluationError):
    """Raised when an undefined function is called."""
    pass


class OperatorNotFoundError(EvaluationError):
    """Raised when an undefined operator is used."""
    pass
