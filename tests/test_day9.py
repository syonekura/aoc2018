import pytest
from aoc import day9


@pytest.mark.parametrize("players, marbles, expected", [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305)
])
def test_high_score(players, marbles, expected):
    assert day9.high_score(players, marbles) == expected
