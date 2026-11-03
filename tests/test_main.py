import pytest
from main import parse_numbers


def test_parse_numbers():
    a, b = parse_numbers(["2", "3"])

    assert a == 2.0
    assert b == 3.0


def test_parse_numbers_invalid():
    with pytest.raises(Exception):
        parse_numbers(["hello", "world"])


def test_parse_numbers_missing():
    with pytest.raises(Exception):
        parse_numbers(["5"])