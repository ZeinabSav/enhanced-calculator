from .operations import get_operation
from .calculation import Calculation
from .history import History
from .calculator_memento import Memento, Caretaker
from .input_validators import validate_number, validate_operation
from .exceptions import CalculatorError


class Calculator:
    """Main calculator facade."""

    def __init__(self, config):
        self.history = History(config.history_file)
        self.caretaker = Caretaker()
        self.config = config

    def calculate(self, a_str: str, b_str: str, op_str: str) -> float:
        """Perform a calculation after validating inputs."""

        # Validate inputs
        a = validate_number(a_str)
        b = validate_number(b_str)
        op_symbol = validate_operation(op_str)

        # Get operation strategy
        operation = get_operation(op_symbol)

        # Save current state for undo
        self.caretaker.save(Memento(self.history.df))

        # Perform calculation
        calc = Calculation(a, b, operation)
        result = calc.perform()

        # Add to history
        self.history.add(a, b, op_symbol, result)

        # Autosave if enabled
        if self.config.autosave:
            self.history.save()

        return result

    def undo(self):
        """Undo last calculation."""
        new_state = self.caretaker.undo(self.history.df)
        if new_state is not None:
            self.history.df = new_state
            if self.config.autosave:
                self.history.save()
        else:
            raise CalculatorError("Nothing to undo.")

    def redo(self):
        """Redo last undone calculation."""
        new_state = self.caretaker.redo(self.history.df)
        if new_state is not None:
            self.history.df = new_state
            if self.config.autosave:
                self.history.save()
        else:
            raise CalculatorError("Nothing to redo.")

    def clear_history(self):
        """Clear all history."""
        self.caretaker.save(Memento(self.history.df))
        self.history.clear()

    def get_history(self):
        """Return the history DataFrame."""
        return self.history.df
