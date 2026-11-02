from save_load import save_history, load_history

def test_save_load():
    history = [["add", 2, 3, 5]]
    save_history(history)

    loaded = load_history()

    assert loaded is not None
    
    from operations import Divide
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(5, 0)