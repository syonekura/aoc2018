from functools import reduce


def process_polymer(example: str):
    def reduction(x, y):
        if len(x) > 0 and _condition(x[-1], y):
            return x[:-1]
        else:
            return x + y
    while True:
        length = len(example)
        example = reduce(reduction, example)
        if len(example) == length:
            return example


def _search_units(value: str):
    for i, (x, y) in enumerate(zip(value[:-1], value[1:])):
        if _condition(x, y):
            return i
    return None


def _condition(x, y) -> bool:
    return x != y and (str.upper(x) == y or str.lower(x) == y)


def shortest_polymer(example):
    return None


if __name__ == '__main__':
    with open('../data/day5.txt') as file:
        polymers = file.read()

    print(f'Units remaining: {len(process_polymer(polymers))}')
