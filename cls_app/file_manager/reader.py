import datetime
from models.event import Event


def read_data_by_date_parameters():
    with open("./data_file.txt", "r") as file:
        lines = [Event(*line.split(' ')) for line in file]
        daily_events = sorted(lines, key=lambda x: x.date == datetime.date(2024, 10, 10))
        return daily_events