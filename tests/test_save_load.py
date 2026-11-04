from save_load import save_history, load_history
import os


def test_save_load():
    history = [["add", 2, 3, 5]]

    save_history(history)

    loaded = load_history()

    assert loaded is not None


def test_load_without_file():
    if os.path.exists("history.csv"):
        os.remove("history.csv")

    result = load_history()

    assert result == []


def test_save_empty_history():
    save_history([])

    loaded = load_history()

    assert loaded is not None