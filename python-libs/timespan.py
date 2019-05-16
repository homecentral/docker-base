from datetime import timedelta

def timespan_seconds(value):
    value = value.lower()
    num = int(value[:-1])

    if value.endswith('s'):
        return timedelta(seconds=num)
    elif value.endswith('m'):
        return timedelta(minutes=num)
    elif value.endswith('h'):
        return timedelta(hours=num)
    elif value.endswith('d'):
        return timedelta(days=num)