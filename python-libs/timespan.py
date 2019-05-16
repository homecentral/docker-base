from datetime import timedelta

def timespan_seconds(value):
    value = value.lower()
    num = float(value[:-1])

    if value.endswith('m'):
        delta = timedelta(minutes=num)
    elif value.endswith('h'):
        delta = timedelta(hours=num)
    elif value.endswith('d'):
        delta = timedelta(days=num)
    else:
        delta = timedelta(seconds=num)

    return delta.total_seconds()