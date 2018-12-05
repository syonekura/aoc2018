import numpy as np
from aoc import day3
import pytest


@pytest.mark.parametrize("claims, width, height, expected", [
    (
        ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"],
        11, 9, 4
    )
])
def test_overlap(claims, width, height, expected):
    assert day3.overlap(claims, width, height) == expected


@pytest.mark.parametrize("fabric", [
    np.zeros(shape=(8, 8), dtype=int)
])
@pytest.mark.parametrize("claim, expected", [
    (
        "#1 @ 1,3: 4x4",
        np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
    ),
    (
        "#2 @ 3,1: 4x4",
        np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
    ),
    (
        '#3 @ 5,5: 2x2',
        np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
    )
])
def test_update_fabric(fabric, claim, expected):
    assert (day3.update_fabric(fabric, claim) == expected).all()
