from .exceptions import InvalidOperationError, CalculatorError


def validate_number(value: str) -> float:
    """Validate that the input is a number."""
    try:
        return float(value)
    except ValueError:
        raise CalculatorError(f"Invalid number: {value}")


def validate_operation(symbol: str):
    """Validate that the operation symbol is allowed."""
    valid_ops = ["+", "-", "*", "/", "^", "root"]
    if symbol not in valid_ops:
        raise InvalidOperationError(f"Invalid operation: {symbol}")
    return symbol


def validate_command(cmd: str):
    """Validate REPL commands."""
    valid_cmds = ["calc", "history", "undo", "redo", "exit", "clear"]
    if cmd not in valid_cmds:
        raise CalculatorError(f"Unknown command: {cmd}")
    return cmd
