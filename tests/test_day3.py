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


@pytest.mark.parametrize("fabric, claim, expected", [
    (
        np.zeros(shape=(8, 8), dtype=int),
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
        np.zeros(shape=(8, 8), dtype=int),
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
        np.zeros(shape=(8, 8), dtype=int),
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


@pytest.mark.parametrize("claims, width, height, expected", [
    (
        ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"],
        11, 9, 3
    )
])
def test_non_overlapping_id(claims, width, height, expected):
    assert day3.non_overlapping_id(claims, width, height) == expected
