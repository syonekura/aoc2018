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


def distribute_work(raw_steps, workers, offset=60):
    instructions = _parse_steps(raw_steps)
    step_graph = _build_graph(instructions)
    all_steps = _get_all_steps(instructions)

    task_times = {t: s + offset for s, t in enumerate(all_steps, start=1)}

    wall = 0
    workers = {i: ('Idle', wall) for i in range(workers)}
    while all_steps:
        # Remove steps performed previously
        performed = {y[0] for x, y in workers.items() if y[1] <= wall and y[0] in all_steps}
        for task in performed:
            all_steps.remove(task)
            try:
                step_graph.pop(task)
            except KeyError:
                pass
        # Select idle workers
        idle = [i for i, v in workers.items() if v[1] <= wall]
        # Select available tasks
        available = [s for s in all_steps if sum(1 if s in v else 0 for _, v in step_graph.items()) == 0
                     and s not in set(v[0] for k, v in workers.items())]
        # Assign tasks to idle workers
        for w, task in zip(idle, available):
            workers[w] = (task, wall + task_times[task])
        # Update wall
        if all_steps:
            wall = min(v[1] for w, v in workers.items() if v[1] > wall)
    return wall


if __name__ == '__main__':
    with open('../data/day7.txt') as file:
        records = file.readlines()
    print(f'Order of steps: {compute_order(records)}')
    print(f'Minimum time: {distribute_work(records, 5)}')
