# tests/test_operations.py

from operations import (
    Add, Subtract, Multiply, Divide,
    Power, Root, Modulus, IntDivide,
    Percent, AbsDiff
)

def test_add():
    assert Add().execute(2, 3) == 5

def test_subtract():
    assert Subtract().execute(5, 3) == 2

def test_multiply():
    assert Multiply().execute(2, 4) == 8

def test_divide():
    assert Divide().execute(8, 2) == 4

def test_power():
    assert Power().execute(2, 3) == 8

def test_root():
    assert round(Root().execute(27, 3), 5) == 3

def test_modulus():
    assert Modulus().execute(10, 3) == 1

def test_int_divide():
    assert IntDivide().execute(10, 3) == 3

def test_percent():
    assert Percent().execute(10, 50) == 5

def test_abs_diff():
    assert AbsDiff().execute(10, 3) == 7
