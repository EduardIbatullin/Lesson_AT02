import pytest
from lw_AT02_2 import check


def test_check():
    assert check(6) == True


def test_check2():
    assert check(3) == False


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (5, False),
        (0, True),
        (56, True),
        (-3, False),
    ],
)
def test_check_with_parameters(number, expected):
    assert check(number) == expected
