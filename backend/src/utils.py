from datetime import datetime


def datetime_from_json(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
