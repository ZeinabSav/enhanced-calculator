# logger.py

import logging
import pandas as pd
from history import history

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

class LoggingObserver:
    def update(self, entry):
        logging.info(
            f"{entry['op']}({entry['a']}, {entry['b']}) = {entry['result']}"
        )

class AutoSaveObserver:
    def __init__(self, csv_path: str = "history.csv"):
        self.csv_path = csv_path

    def update(self, entry):
        df = pd.DataFrame(history)
        df.to_csv(self.csv_path, index=False)
