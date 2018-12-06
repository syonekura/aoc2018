import pytest
import random
from aoc import day4
from datetime import date

records = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
""".rstrip('\n')


@pytest.mark.parametrize("rec, expected", [
    (records, 240)
])
def test_strategy_1(rec, expected):
    assert day4.strategy_1(rec) == expected


def test_sort_records():
    shuffled = records.splitlines()
    random.shuffle(shuffled)
    shuffled = '\n'.join(shuffled)
    assert day4.sort_records(shuffled) == records


@pytest.mark.parametrize("record, expected", [
    ('[1518-11-01 00:00] Guard #10 begins shift', date(1518, 11, 1)),
    ('[1518-11-02 00:50] wakes up', date(1518, 11, 2))
])
def test_parse_date(record, expected):
    assert day4.parse_date(record) == expected


@pytest.mark.parametrize("record, expected", [
    ('[1518-11-01 00:05] Guard #10 begins shift', 5),
    ('[1518-11-02 00:50] wakes up', 50),
    ('[1518-11-01 23:58] Guard #99 begins shift', 0)
])
def test_parse_time(record, expected):
    assert day4.parse_time(record) == expected


@pytest.mark.parametrize("record, expected", [
    ('[1518-11-01 00:05] Guard #10 begins shift', 'begins shift'),
    ('[1518-11-02 00:50] wakes up', 'wakes up'),
    ('[1518-11-03 00:24] falls asleep', 'falls asleep')
])
def test_parse_event(record, expected):
    assert day4.parse_event(record) == expected


@pytest.mark.parametrize("record, expected", [
    ('[1518-11-01 00:05] Guard #10 begins shift', 10),
    ('[1518-11-02 00:50] wakes up', None),
    ('[1518-11-03 00:24] falls asleep', None)
])
def test_parse_id(record, expected):
    assert day4.parse_id(record) == expected
