# config.py

from dotenv import load_dotenv
import os

load_dotenv()

PRECISION = int(os.getenv("PRECISION", "4"))
AUTOSAVE = os.getenv("AUTOSAVE", "true").lower() == "true"
CSV_PATH = os.getenv("CSV_PATH", "history.csv")
