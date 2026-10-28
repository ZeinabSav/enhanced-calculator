# tests/test_history.py

from history import HistoryManager

def test_undo_redo():
    h = HistoryManager()
    e1 = h.add_entry("add", 1, 2, 3)
    e2 = h.add_entry("add", 2, 3, 5)

    assert len(h.get_history()) == 2

    u = h.undo()
    assert u == e2
    assert len(h.get_history()) == 1

    r = h.redo()
    assert r == e2
    assert len(h.get_history()) == 2
