from datetime import datetime, date
import re


def sort_records(shuffled: str):
    return '\n'.join(list(sorted(shuffled.splitlines())))


def parse_date(record) -> date:
    return datetime.strptime(record[0:18], '[%Y-%m-%d %H:%M]').date()


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


def strategy_1(rec):
    return None