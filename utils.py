import datetime


def _json_encode(obj):
    if isinstance(obj, str):
        return str(obj)
    elif isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError(repr(obj) + " is not JSON serializable")