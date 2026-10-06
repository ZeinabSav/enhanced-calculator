class CalculatorError(Exception):
    """Base class for calculator errors."""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when an unknown operation is requested."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass


class ConfigError(CalculatorError):
    """Raised when configuration loading fails."""
    pass
