from itertools import cycle
from collections import deque


def high_score(players, marbles):
    circle = deque([0])
    scores = [0 for _ in range(players)]

    for marble, player in zip(range(1, marbles+1), cycle(range(players))):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return max(scores)


if __name__ == '__main__':
    print(f'High score {high_score(477, 70851)}')
    print(f'High score {high_score(477, 7085100)}')
