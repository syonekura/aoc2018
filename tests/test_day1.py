import pytest
from aoc import day1


@pytest.mark.parametrize("arg, expected", [
    (['+1', '+1', '+1'], 3),
    (['+1', '+1', '-2'], 0),
    (['-1', '-2', '-3'], -6)
])
def chronal_calibration(arg, expected):
    assert day1.chronal_calibration(arg) == expected
