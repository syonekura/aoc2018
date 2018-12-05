from itertools import groupby, combinations
from typing import List, Set


def char_summary(arg: str) -> dict:
    data = sorted(arg)
    result = {1: 0, 2: 0, 3: 0}
    for k, g in groupby(data):
        aux = len(list(g))
        if aux in result.keys():
            result[aux] += 1
    return result


def checksum(arg: List[str]) -> int:
    count_twos = 0
    count_threes = 0

    for code in arg:
        summary = char_summary(code)

        if summary[2] > 0:
            count_twos += 1
        if summary[3] > 0:
            count_threes += 1
    return count_twos * count_threes


def string_distance(str1: str, str2: str) -> int:
    return sum(1 if x != y else 0 for x, y in zip(str1, str2))


def remove_diff(value1, value2):
    return ''.join(x for x, y in zip(value1, value2) if x == y)


def detect_ids(ids: List[str]) -> Set[str]:
    ids = sorted(ids)
    for x, y in combinations(ids, 2):
        if string_distance(x, y) == 1:
            return {x, y}


if __name__ == '__main__':
    with open('../data/day2/checksum.txt') as file:
        values = file.readlines()
    print(f'Checksum: {checksum(values)}')
    detected_ids = detect_ids(values)
    print(f'Correct IDs: { remove_diff(*list(detected_ids)) }')
