class Memento:
    """Stores the calculator state for undo/redo."""

    def __init__(self, history_df):
        # We store a COPY of the DataFrame to avoid accidental changes
        self.state = history_df.copy()


class Caretaker:
    """Manages undo and redo stacks."""

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, memento: Memento):
        """Save a new state to the undo stack."""
        self.undo_stack.append(memento)
        # Clear redo stack whenever a new action happens
        self.redo_stack.clear()

    def undo(self, current_state):
        """Undo: return previous state and push current to redo."""
        if not self.undo_stack:
            return None

        self.redo_stack.append(Memento(current_state))
        return self.undo_stack.pop().state

    def redo(self, current_state):
        """Redo: return next state and push current to undo."""
        if not self.redo_stack:
            return None

        self.undo_stack.append(Memento(current_state))
        return self.redo_stack.pop().state
