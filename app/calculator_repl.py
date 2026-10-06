from .calculator import Calculator
from .calculator_config import CalculatorConfig
from .input_validators import validate_command
from .exceptions import CalculatorError


class CalculatorREPL:
    """Command-line interface for the calculator."""

    def __init__(self):
        self.config = CalculatorConfig()
        self.calculator = Calculator(self.config)

    def start(self):
        print("Enhanced Calculator — type 'exit' to quit.")

        while True:
            try:
                cmd = input("\nEnter command (calc/history/undo/redo/clear/exit): ").strip()
                cmd = validate_command(cmd)

                if cmd == "exit":
                    print("Goodbye!")
                    break

                elif cmd == "calc":
                    a = input("Enter first number: ")
                    b = input("Enter second number: ")
                    op = input("Enter operation (+, -, *, /, ^, root): ")

                    result = self.calculator.calculate(a, b, op)
                    print(f"Result: {result}")

                elif cmd == "history":
                    print("\nCalculation History:")
                    print(self.calculator.get_history())

                elif cmd == "undo":
                    self.calculator.undo()
                    print("Undo complete.")

                elif cmd == "redo":
                    self.calculator.redo()
                    print("Redo complete.")

                elif cmd == "clear":
                    self.calculator.clear_history()
                    print("History cleared.")

            except CalculatorError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
