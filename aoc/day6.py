from itertools import product, chain


def largest_area(coords):
    coords = list(sorted(coords))

    # Calculate boundary
    xs = (x for x, _ in coords)
    ys = (y for _, y in coords)
    boundary = {(x, y) for x, y in chain(
        product(range(min(xs), max(xs) + 1), {min(ys), max(ys)}),
        product({min(xs), max(xs)}, range(min(ys), max(ys) + 1))
    )}

    return None