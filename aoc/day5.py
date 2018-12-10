from functools import reduce
import string


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


def _condition(x, y) -> bool:
    return x != y and (str.upper(x) == y or str.lower(x) == y)


def shortest_polymer(example: str):
    a = [(len(process_polymer(example.replace(low, '').replace(up, ''))), low)
         for low, up in zip(string.ascii_lowercase, string.ascii_uppercase)]
    return min(a, key=lambda x: x[0])


if __name__ == '__main__':
    with open('../data/day5.txt') as file:
        polymers = file.read()

    print(f'Units remaining: {len(process_polymer(polymers))}')
    print(f'Shortest Polymer: {shortest_polymer(polymers)}')
