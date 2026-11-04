from unittest.mock import patch
from main import parse_numbers
import pytest


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


def test_parse_numbers_negative():
    a, b = parse_numbers(["-5", "-10"])

    assert a == -5.0
    assert b == -10.0


def test_parse_numbers_decimal():
    a, b = parse_numbers(["2.5", "3.5"])

    assert a == 2.5
    assert b == 3.5

    from unittest.mock import patch
from main import main


def test_main_exit():
    with patch("builtins.input", side_effect=["exit"]):
        main()


def test_main_help():
    with patch("builtins.input", side_effect=["help", "exit"]):
        main()


def test_main_history():
    with patch("builtins.input", side_effect=["history", "exit"]):
        main()


def test_main_bad_command():
    with patch("builtins.input", side_effect=["fakecommand", "exit"]):
        main()