import pytest
from aoc import day6


@pytest.mark.parametrize("coords, expected", [
    ([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)],
     17)
])
def test_largest_area(coords, expected):
    assert day6.largest_area(coords) == expected


@pytest.mark.parametrize("coords, sum_dist, expected", [
    ([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)],
     32, 16)
])
def test_safe_zone(coords, sum_dist, expected):
    assert day6.safe_zone(coords, sum_dist) == expected
