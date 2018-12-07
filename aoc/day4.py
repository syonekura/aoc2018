from datetime import datetime, date, timedelta
import re
import numpy as np
from itertools import groupby
from functools import reduce


def sort_records(shuffled: str):
    return list(sorted(shuffled.splitlines()))


def parse_date(record) -> date:
    timestamp = datetime.strptime(record[0:18], '[%Y-%m-%d %H:%M]')
    if timestamp.time().hour > 0:
        dt = timestamp.date()
        return date(dt.year, dt.month, dt.day) + timedelta(days=1)
    else:
        return timestamp.date()


def parse_time(record) -> int:
    record_time = datetime.strptime(record[0:18], '[%Y-%m-%d %H:%M]').time()
    if record_time.hour > 0:
        return 0
    else:
        return record_time.minute


def parse_event(record):
    if 'begins shift' in record:
        return 'begins shift'
    elif 'wakes up' in record:
        return 'wakes up'
    elif 'falls asleep' in record:
        return 'falls asleep'
    return None


def parse_id(record):
    pattern = re.compile(r'.*\s#(\d+)\s.*')
    if pattern.match(record):
        return int(pattern.sub('\\1', record))
    else:
        return None


def parse_records(rec):
    records = sort_records(rec)
    dates = map(parse_date, records)
    minutes = map(parse_time, records)
    events = map(parse_event, records)
    ids = map(parse_id, records)
    records = dict()
    last_id = None
    for dt, minute, event, gid in zip(dates, minutes, events, ids):
        if gid is not None:
            last_id = gid

        if event == 'begins shift':
            if last_id not in records.keys():
                records[last_id] = dict()
            records[last_id][dt] = np.zeros(60, dtype=int)
        elif event == 'falls asleep':
            records[last_id][dt][minute] = 1
        elif event == 'wakes up':
            asleep = np.where(records[last_id][dt] == 1)[0].max()
            records[last_id][dt][asleep:minute] = 1
    return records


def strategy_1(rec):
    # Parse records
    records = parse_records(rec)
    # Guard that sleeps the most
    aux = sorted((gid, sum(mins))
                 for gid, y in records.items()
                 for _, mins in y.items())
    sleeper = max(((gid, reduce(lambda x, y: x + y[1], group, 0))
                   for gid, group
                   in groupby(aux, key=lambda x: x[0])),
                  key=lambda x: x[1])
    # Minute that sleeps more often
    minute = np.argmax(reduce(lambda x, y: x + y,
                              records[sleeper[0]].values()))
    return sleeper[0] * minute


def strategy_2(rec):
    records = parse_records(rec)
    # Frequency among minutes
    freq = {(gid, np.argmax(mins), max(mins))
            for gid, mins in ((gid, reduce(lambda x, y: x+y, value.values()))
                              for gid, value in records.items())}
    max_freq = max(freq, key=lambda x: x[2])
    return max_freq[0] * max_freq[1]


if __name__ == '__main__':
    with open('../data/day4.txt') as file:
        recs = file.read()
    print(f'Strategy 1: {strategy_1(recs)}')
    print(f'Strategy 2: {strategy_2(recs)}')
