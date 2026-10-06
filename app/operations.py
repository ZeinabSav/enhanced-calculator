from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Perform the operation on a and b."""
        pass
class Addition(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtraction(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiplication(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a * b


class Division(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class Power(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a ** b


class Root(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        # b is the root degree
        if b == 0:
            raise ZeroDivisionError("Cannot take root with degree 0.")
        return a ** (1 / b)

from .exceptions import InvalidOperationError  # you'll create this later


def get_operation(symbol: str) -> OperationStrategy:
    if symbol == "+":
        return Addition()
    elif symbol == "-":
        return Subtraction()
    elif symbol == "*":
        return Multiplication()
    elif symbol == "/":
        return Division()
    elif symbol == "^":
        return Power()
    elif symbol == "root":
        return Root()
    else:
        raise InvalidOperationError(f"Unknown operation: {symbol}")
from .exceptions import InvalidOperationError  # you'll create this later


def get_operation(symbol: str) -> OperationStrategy:
    if symbol == "+":
        return Addition()
    elif symbol == "-":
        return Subtraction()
    elif symbol == "*":
        return Multiplication()
    elif symbol == "/":
        return Division()
    elif symbol == "^":
        return Power()
    elif symbol == "root":
        return Root()
    else:
        raise InvalidOperationError(f"Unknown operation: {symbol}")
