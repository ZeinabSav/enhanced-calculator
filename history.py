# history.py

from datetime import datetime

history: list[dict] = []
redo_stack: list[dict] = []

class HistoryManager:
    def add_entry(self, op_name, a, b, result):
        entry = {
            "op": op_name,
            "a": a,
            "b": b,
            "result": result,
            "timestamp": datetime.now().isoformat(),
        }
        history.append(entry)
        redo_stack.clear()
        return entry

    def undo(self):
        if not history:
            return None
        entry = history.pop()
        redo_stack.append(entry)
        return entry

    def redo(self):
        if not redo_stack:
            return None
        entry = redo_stack.pop()
        history.append(entry)
        return entry

    def get_history(self):
        return list(history)

    def clear(self):
        history.clear()
        redo_stack.clear()
