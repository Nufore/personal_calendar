import datetime
from models.event import Event
from serializers.event_serializer import serialize_event


def read_data_by_date_parameters(day: datetime.date):
    with open("./data_file.txt", "r") as file:
        daily_events = []
        for line in file:
            data = line.split(' ')

            date = datetime.date(*list(map(int, data[0].split('-'))))
            if not datetime.date.today() <= date <= day:
                continue
            time = datetime.time(*list(map(int, data[1].split(":"))))
            category = data[2]
            title = data[3]
            description = data[4][:-1]

            event = Event(date, time, category, title, description)
            daily_events.append(event)

        return daily_events


def get_line_id_from_file_by_date(date: datetime.date) -> list:
    id_line_list = []
    with open("./data_file.txt", "r") as file:
        lines = file.readlines()
        for line_id, line in enumerate(lines):
            if serialize_event(line=line).date == date:
                id_line_list.append((line_id, line))

    return id_line_list
