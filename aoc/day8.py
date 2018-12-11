def sum_metadata(licence: str):
    licence = list(map(int, licence.split(' ')))
    totals, value, _ = parse_tree(licence)
    return totals, value


def parse_tree(data):
    children, metas = data[:2]
    data = data[2:]
    totals = 0
    scores = []

    for c in range(children):
        total, score, data = parse_tree(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return totals, sum(data[:metas]), data[metas:]
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if 0 < k <= len(scores)),
            data[metas:]
        )


if __name__ == '__main__':
    with open('../data/day8.txt') as file:
        licence_data = file.read()

    total, value = sum_metadata(licence_data)
    print(f'Metadata Sum: {total}')
    print(f'Value: {value}')

