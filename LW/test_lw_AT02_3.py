import pytest
from lw_AT02_3 import is_palindrome


def test_is_palindrome_true():
    assert is_palindrome("мадам") == True


def test_is_palindrome_false():
    assert is_palindrome("чулок") == False


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("level", True),
        ("python", False),
        ("racecar", True),
        ("", True),
    ],
)
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
