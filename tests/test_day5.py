from aoc import day5
import pytest


@pytest.mark.parametrize("example, expected", [
    ('dabAcCaCBAcCcaDA', 'dabCBAcaDA')
])
def test_example(example, expected):
    assert day5.process_polymer(example) == expected
