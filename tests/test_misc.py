from config import PRECISION
from exceptions import OperationError
from save_load import save_history, load_history

def test_config():
    assert PRECISION is not None

def test_exception():
    e = OperationError("test")
    assert str(e) == "test"

def test_save_load():
    history = [["add", 2, 3, 5]]

    save_history(history)

    result = load_history()

    assert result is not None