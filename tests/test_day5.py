from aoc import day5
import pytest


@pytest.mark.parametrize("example, expected", [
    ('dabAcCaCBAcCcaDA', 'dabCBAcaDA')
])
def test_example(example, expected):
    assert day5.process_polymer(example) == expected


@pytest.mark.parametrize("example, expected", [
    ('dabAcCaCBAcCcaDA', (4, 'c'))
])
def test_shortest_polymer(example, expected):
    assert day5.shortest_polymer(example) == expected
