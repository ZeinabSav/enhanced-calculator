import pandas as pd
from pathlib import Path


class History:
    """Manages calculation history using pandas."""

    def __init__(self, file_path: str = "history.csv"):
        self.file_path = Path(file_path)

        # Create empty DataFrame if file doesn't exist
        if not self.file_path.exists():
            self.df = pd.DataFrame(columns=["a", "b", "operation", "result"])
        else:
            self.df = pd.read_csv(self.file_path)

    def add(self, a: float, b: float, operation: str, result: float):
        """Add a new calculation to history."""
        new_row = {"a": a, "b": b, "operation": operation, "result": result}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def save(self):
        """Save history to CSV."""
        self.df.to_csv(self.file_path, index=False)

    def load(self):
        """Reload history from CSV."""
        if self.file_path.exists():
            self.df = pd.read_csv(self.file_path)

    def clear(self):
        """Clear history."""
        self.df = pd.DataFrame(columns=["a", "b", "operation", "result"])
        self.save()
