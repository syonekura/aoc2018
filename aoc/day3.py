import re
import numpy as np


def update_fabric(fabric, claim) -> np.ndarray:
    pattern = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
    id, x, y, width, height = tuple(
        int(x) for x in pattern.sub('\\1 \\2 \\3 \\4 \\5', claim).split())
    fabric[y:(y+height), x:(x+width)] += 1
    return fabric


def overlap(claims, width, height) -> int:
    fabric = np.zeros(shape=(width, height))
    for claim in claims:
        fabric = update_fabric(fabric, claim)
    return np.sum(fabric > 1, dtype=np.int)


if __name__ == '__main__':
    with open('../data/day3/claims') as file:
        claims = file.readlines()
    print(f'Overlapping fabric: {overlap(claims, 1000, 1000)}')
