import re
import datetime


def set_date():
    input_date: str = input("Введите дату события: ")
    pattern = r"\d\d\d\d[-]\d\d[-]\d\d"
    if re.fullmatch(pattern=pattern, string=input_date):
        returned_date = datetime.date(*list(map(int, input_date.split('-'))))
        return returned_date
    else:
        return set_date()


def set_time():
    input_time: str = input("Введите время события: ")
    pattern = r"\d\d[:]\d\d"
    if re.fullmatch(pattern=pattern, string=input_time):
        try:
            returned_time = datetime.time(*list(map(int, input_time.split(":"))))
            return returned_time
        except ValueError as e:
            print(e.__repr__())
            return set_time()
    else:
        return set_time()


def set_type():
    event_types = ["работа", "личное", "отдых"]
    input_type = int(input("Введите категорию события:\n1 - работа\n2 - личное\n3 - отдых\n"))
    if input_type == 1:
        return event_types[input_type - 1]
    elif input_type == 2:
        return event_types[input_type - 1]
    elif input_type == 3:
        return event_types[input_type - 1]
    else:
        return set_type()


def set_title():
    event_title = input("Введите заголовок события: ")
    return event_title.replace(" ", "_")


def set_description():
    event_description = input("Введите описание события: ")
    return event_description.replace(" ", "_")
