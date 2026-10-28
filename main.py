# main.py

from operations import get_operation
from history import HistoryManager
from logger import LoggingObserver, AutoSaveObserver
from config import PRECISION, AUTOSAVE, CSV_PATH
from exceptions import OperationError, ValidationError

history_manager = HistoryManager()
observers = [LoggingObserver()]
if AUTOSAVE:
    observers.append(AutoSaveObserver(CSV_PATH))


def print_help():
    print("Commands:")
    print("  add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
    print("  history, undo, redo, clear, help, exit")


def parse_numbers(args):
    if len(args) < 2:
        raise ValidationError("Need two numbers")
    try:
        a = float(args[0])
        b = float(args[1])
        return a, b
    except ValueError:
        raise ValidationError("Invalid number(s)")


def main():
    print("Enhanced Calculator REPL. Type 'help' for commands.")
    while True:
        try:
            cmd = input("> ").strip().split()
            if not cmd:
                continue

            name = cmd[0]

            if name == "exit":
                break
            elif name == "help":
                print_help()
            elif name == "history":
                for e in history_manager.get_history():
                    print(e)
            elif name == "clear":
                history_manager.clear()
                print("History cleared.")
            elif name == "undo":
                e = history_manager.undo()
                print("Undo:", e if e else "Nothing to undo")
            elif name == "redo":
                e = history_manager.redo()
                print("Redo:", e if e else "Nothing to redo")
            else:
                op = get_operation(name)
                if op is None:
                    raise OperationError(f"Unknown operation: {name}")

                a, b = parse_numbers(cmd[1:])
                result = op.execute(a, b)
                result_rounded = round(result, PRECISION)
                entry = history_manager.add_entry(name, a, b, result_rounded)

                for obs in observers:
                    obs.update(entry)

                print(result_rounded)

        except (OperationError, ValidationError, ZeroDivisionError) as e:
            print("Error:", e)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
