from typing import List


def chronal_calibration(input: List[str]):
    return sum(int(x) for x in input)


if __name__ == '__main__':
    with open('../data/day1/chronal_calibration.txt') as file:
        text_input = file.readlines()
    print(chronal_calibration(text_input))
