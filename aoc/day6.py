from itertools import product, chain
from collections import defaultdict


def _manhattan(x, y, coords):
    dist = map(lambda p: (abs(p[0] - x) + abs(p[1] - y)), coords)
    return dist


def _closest(x, y, coords):
    dist = _manhattan(x, y, coords)
    dist = iter(sorted(enumerate(dist), key=lambda d: d[1]))
    d1 = next(dist)
    d2 = next(dist)
    if d1[1] < d2[1]:
        return d1[0]
    else:
        return None


def _calculate_limits(coords):
    minx = min(coords, key=lambda x: x[0])[0]
    maxx = max(coords, key=lambda x: x[0])[0]
    miny = min(coords, key=lambda y: y[1])[1]
    maxy = max(coords, key=lambda y: y[1])[1]
    return maxx, maxy, minx, miny


def largest_area(coords):
    coords = list(sorted(coords))

    # Calculate boundary
    maxx, maxy, minx, miny = _calculate_limits(coords)
    boundary = {(x, y) for x, y in chain(
        product(range(minx, maxx + 1), {miny, maxy}),
        product({minx, maxx}, range(miny, maxy + 1))
    )}

    points = {(x, y): _closest(x, y, coords) for x, y in
              product(range(minx, maxx + 1), range(miny, maxy + 1))
              if _closest(x, y, coords) is not None}

    areas = defaultdict(set)
    for k, v in points.items():
        areas[v].add(k)
    areas = {(k, len(v)) for k, v in areas.items() if boundary.isdisjoint(v)}
    max_area = max(areas, key=lambda x: x[1])

    return max_area[1]


def safe_zone(coords, sum_dist):
    maxx, maxy, minx, miny = _calculate_limits(coords)
    points = {(x, y): sum(_manhattan(x, y, coords)) for x, y in
              product(range(minx, maxx + 1), range(miny, maxy + 1))
              if sum(_manhattan(x, y, coords)) < sum_dist
    }
    return len(points)


if __name__ == '__main__':
    with open('../data/day6.txt') as file:
        coordinates = [tuple(map(int, x.split(','))) for x in file.readlines()]
    print(f'Largest finite area: {largest_area(coordinates)}')
    print(f'Largest Safe Zone: {safe_zone(coordinates, 10000)}')
