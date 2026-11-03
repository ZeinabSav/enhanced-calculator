from save_load import save_history, load_history

def test_save_load():
    history = [["add", 2, 3, 5]]

    save_history(history)

    result = load_history()

    assert result is not None

def test_load_without_file():
    result = load_history()

    assert result is not None

    from save_load import save_history, load_history


def test_save_load():
    history = [["add", 2, 3, 5]]

    save_history(history)

    loaded = load_history()

    assert loaded is not None


def test_load_without_file():
    result = load_history()

    assert result is not None