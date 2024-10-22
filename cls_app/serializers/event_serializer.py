import datetime
from models.event import Event


def serialize_event(line: str) -> Event:
    data = line.split(' ')

    date = datetime.date(*list(map(int, data[0].split('-'))))
    time = datetime.time(*list(map(int, data[1].split(":"))))
    category = data[2]
    title = data[3]
    description = data[4][:-1]

    event = Event(date, time, category, title, description)

    return event
