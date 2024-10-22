import datetime

from file_manager.reader import read_data_by_date_parameters


def read_data_all(date_delta):
    events = read_data_by_date_parameters(day=date_delta)
    if events:
        for event in events:
            print(event)
    else:
        print("Событий не найдено\n")


def reading_all():
    reading_all_type = input("d - на день\nw - на неделю\nm - на месяц\n")
    if reading_all_type == "d":
        read_data_all(date_delta=datetime.date.today())
    elif reading_all_type == "w":
        read_data_all(date_delta=datetime.date.today() + datetime.timedelta(7))
    elif reading_all_type == "m":
        read_data_all(date_delta=datetime.date.today() + datetime.timedelta(30))
    else:
        return reading_all()


def reading_one():
    print("ZAGLUSHKA")
