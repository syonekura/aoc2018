from itertools import accumulate, cycle
from typing import List


def as_int(text):
    for x in text:
        yield int(x)


def chronal_calibration(text: List[str]):
    return sum(as_int(text))


def twice_frequency(text):
    frequencies = {0}
    for freq in accumulate(cycle(as_int(text))):
        if freq in frequencies:
            return freq
        else:
            frequencies.add(freq)


if __name__ == '__main__':
    with open('../data/day1/chronal_calibration.txt') as file:
        text_input = file.readlines()
    print(f'Day 1 Part 1: {chronal_calibration(text_input)}')
    print(f'Day 1 Part 2: {twice_frequency(text_input)}')
