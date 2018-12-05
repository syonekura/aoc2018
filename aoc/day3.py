import re
import numpy as np
from itertools import product


def update_fabric(fabric, claim) -> np.ndarray:
    _, x, y, width, height = parse_claim(claim)
    fabric[y:(y+height), x:(x+width)] += 1
    return fabric


def parse_claim(claim):
    pattern = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
    return tuple(
        int(x) for x in pattern.sub('\\1 \\2 \\3 \\4 \\5', claim).split())


def union(claims, height, width):
    fabric = np.zeros(shape=(width, height))
    for claim in claims:
        fabric = update_fabric(fabric, claim)
    return fabric


def overlap(claims, width, height) -> int:
    fabric = union(claims, height, width)
    return int(np.sum(fabric > 1))


def non_overlapping_id(claims, width, height):
    fabric = union(claims, width, height)
    I, J = np.where(fabric == 1)
    superset = {(x, y) for x, y in zip(I, J)}
    parsed_claims = {parse_claim(claim) for claim in claims}
    claims = {cid: set(product(range(y, y+height), range(x, x+width)))
              for cid, x, y, width, height in parsed_claims}
    cid = next(cid for cid, claim in claims.items()
               if claim.issubset(superset))
    return cid


if __name__ == '__main__':
    with open('../data/day3/claims') as file:
        claims = file.readlines()
    print(f'Overlapping fabric: {overlap(claims, 1000, 1000)}')
    print(f'Non overlapping id: {non_overlapping_id(claims, 1000, 1000)}')
