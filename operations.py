# operations.py

import math

class Operation:
    def execute(self, a, b=None):
        raise NotImplementedError

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

class Multiply(Operation):
    def execute(self, a, b):
        return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot take root with degree 0")
        return a ** (1 / b)

class Modulus(Operation):
    def execute(self, a, b):
        return a % b

class IntDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a // b

class Percent(Operation):
    def execute(self, a, b):
        # a percent of b
        return (a / 100.0) * b

class AbsDiff(Operation):
    def execute(self, a, b):
        return abs(a - b)


def get_operation(name: str) -> Operation | None:
    ops = {
        "add": Add(),
        "subtract": Subtract(),
        "multiply": Multiply(),
        "divide": Divide(),
        "power": Power(),
        "root": Root(),
        "modulus": Modulus(),
        "int_divide": IntDivide(),
        "percent": Percent(),
        "abs_diff": AbsDiff(),
    }
    return ops.get(name)
