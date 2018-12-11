import re
from collections import defaultdict


def _parse_steps(raw_steps):
    pattern = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin\.')
    steps = list(list(map(str.strip, pattern.sub('\\1 \\2', x).split(' '))) for x in raw_steps)
    return steps


def _build_graph(steps):
    # Build graph
    step_graph = defaultdict(set)
    for step in steps:
        step_graph[step[0]].add(step[1])
    return step_graph


def _get_all_steps(instructions):
    all_steps = list(sorted(set(x[0] for x in instructions).union(x[1] for x in instructions)))
    return all_steps


def compute_order(raw_steps):
    instructions = _parse_steps(raw_steps)
    step_graph = _build_graph(instructions)
    all_steps = _get_all_steps(instructions)
    # Search order
    result = ''
    while all_steps:
        for step in all_steps:
            dependencies = sum(1 if step in v else 0 for k, v in step_graph.items())
            if dependencies == 0:
                result += step
                all_steps.remove(step)
                try:
                    step_graph.pop(step)
                except KeyError:
                    pass
                break
    return result


if __name__ == '__main__':
    with open('../data/day7.txt') as file:
        records = file.readlines()
    print(f'Order of steps: {compute_order(records)}')
