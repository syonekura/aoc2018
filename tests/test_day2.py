import pytest
from aoc import day2


@pytest.mark.parametrize("arg, expected", [
    ('abcdef', {1: 6, 2: 0, 3: 0}),
    ('bababc', {1: 1, 2: 1, 3: 1}),
    ('abbcde', {1: 4, 2: 1, 3: 0}),
    ('abcccd', {1: 3, 2: 0, 3: 1}),
    ('aabcdd', {1: 2, 2: 2, 3: 0}),
    ('abcdee', {1: 4, 2: 1, 3: 0}),
    ('ababab', {1: 0, 2: 0, 3: 2})
])
def test_char_summary(arg, expected):
    assert day2.char_summary(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    (
            ['abcdef', 'bababc', 'abbcde', 'abcccd',
             'aabcdd', 'abcdee', 'ababab'], 12
    )
])
def test_checksum(arg, expected):
    assert day2.checksum(arg) == expected


@pytest.mark.parametrize("str1, str2, expected", [
    ('abcde', 'axcye', 2),
    ('fghij', 'fguij', 1)
])
def test_string_distance(str1, str2, expected):
    assert day2.string_distance(str1, str2) == expected


@pytest.mark.parametrize("ids, expected", [
    (
        ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"],
        {'fghij', 'fguij'}
    )
])
def test_detect_ids(ids, expected):
    assert day2.detect_ids(ids) == expected


@pytest.mark.parametrize("value1, value2, expected", [
    ('fghij', 'fguij', 'fgij')
])
def test_remove_diff(value1, value2, expected):
    assert day2.remove_diff(value1, value2) == expected
