import pytest
from aoc import day1


@pytest.mark.parametrize("arg, expected", [
    (['+1', '+1', '+1'], 3),
    (['+1', '+1', '-2'], 0),
    (['-1', '-2', '-3'], -6)
])
def chronal_calibration(arg, expected):
    assert day1.chronal_calibration(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ('+1, -1'.split(','), 0),
    ('+3, +3, +4, -2, -4'.split(','), 10),
    ('-6, +3, +8, +5, -6'.split(','), 5),
    ('+7, +7, -2, -7, -4'.split(','), 14)
])
def test_twice_frequency(arg, expected):
    assert day1.twice_frequency(arg) == expected
