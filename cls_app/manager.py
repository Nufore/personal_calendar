from crud.create_event import create_event
from crud.read_event import reading_all, reading_one
from crud.update_event import get_id_to_update_event
from file_manager.writer import write_to_file
from file_manager.reader import get_line_id_from_file_by_date
from file_manager.updater import update_file_by_line_id
from event_validators.input_and_validate_params import set_date, set_time, set_type, set_title, set_description

def add_event():
    new_event = create_event()
    print(write_to_file(file_name="./data_file.txt", text=new_event.__repr__()))


def read_events():
    reading_type = input("Вывод события/событий:\nall - всех событий\none - конкретное событие\n")
    if reading_type == "all":
        reading_all()
    elif reading_type == "one":
        reading_one()


def update_events():
    date = set_date()
    id_line_list = get_line_id_from_file_by_date(date=date)
    if id_line_list:
        event_id = get_id_to_update_event(id_line_list)
        update_file_by_line_id(event_id)

def start_runner():
    while True:
        print("Введите команду\n1 - Добавить событие\n2 - Вывод событий\n3 - Редактировать событие")
        command = input()
        if command == "1":
            add_event()
        elif command == "2":
            read_events()
        elif command == "3":
            update_events()