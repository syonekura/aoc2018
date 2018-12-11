from aoc import day7

example = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".rstrip('\n').lstrip('\n').splitlines()


def test_order():
    assert day7.compute_order(example) == 'CABDFE'
