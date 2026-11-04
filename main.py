# main.py
from colorama import Fore, Style
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
    print("add, subtract, multiply, divide, power, root")
    print("modulus, int_divide, percent, abs_diff")
    print("history, clear, undo, redo, help, exit")


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
                for item in history_manager.get_history():
                    print(item)

            elif name == "clear":
                history_manager.clear()
                print("History cleared.")

            elif name == "undo":
                item = history_manager.undo()
                print("Undo:", item if item else "Nothing to undo")

            elif name == "redo":
                item = history_manager.redo()
                print("Redo:", item if item else "Nothing to redo")

            else:
                op = get_operation(name)

                if op is None:
                    raise OperationError(f"Unknown operation: {name}")

                a, b = parse_numbers(cmd[1:])

                result = op.execute(a, b)
                result = round(result, PRECISION)

                entry = history_manager.add_entry(
                    name,
                    a,
                    b,
                    result
                )

                for observer in observers:
                    observer.update(entry)

                print(Fore.GREEN + str(result) + Style.RESET_ALL)

        except (OperationError, ValidationError, ZeroDivisionError) as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()