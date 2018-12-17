import numpy as np
import re
from itertools import count


def parse_points(points):
    pattern = re.compile(r'position=<(\s+)?(-?\d+),(\s+)?(-?\d+)>\svelocity=<(\s+)?(-?\d+),(\s+)?(-?\d+)>')
    position = np.array([(int(pattern.sub('\\2', x)), int(pattern.sub('\\4', x))) for x in points], dtype=int)
    velocity = np.array([(int(pattern.sub('\\6', x)), int(pattern.sub('\\8', x))) for x in points], dtype=int)
    return position, velocity


def search_min(position: np.ndarray, velocity: np.ndarray):
    position = position.copy()
    velocity = velocity.copy()
    best_time = 0
    best_area = np.inf
    for i in count():
        min_x, min_y = (position + i * velocity).min(axis=0)
        max_x, max_y = (position + i * velocity).max(axis=0)

        area = abs(max_x - min_x) * abs(max_y - min_y)
        if area < best_area:
            best_time = i
            best_area = area
        else:
            break

    return best_time, best_area


def build_str_at(time: int, pos: np.ndarray, vel: np.ndarray):
    val = pos.copy() + time * vel.copy()
    val -= val.min(axis=0)
    max_x, max_y = val.max(axis=0)
    canvas = np.zeros((max_x + 1, max_y + 1), dtype=int)
    canvas[val[:, 0], val[:, 1]] = 8
    canvas = canvas.transpose().tolist()
    result = ''
    for row in canvas:
        for x in row:
            result += '#' if x == 8 else ' '
        result += '\n'
    return result


if __name__ == '__main__':
    with open('../data/day10.txt') as file:
        pos, vel = parse_points(file.readlines())

    time, area = search_min(pos, vel)
    print(f'Constellation: \n{build_str_at(time, pos, vel)}')
    print(f'Seconds: {time}')