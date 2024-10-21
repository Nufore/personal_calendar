from crud.create_event import create_event
from crud.read_event import reading_all, reading_one
from file_manager.writer import write_to_file
from event_validators.input_and_validate_params import set_date, set_time, set_type, set_title, set_description

def add_event():
    event_data = [set_date(), set_time(), set_type(), set_title(), set_description()]
    new_event = create_event(*event_data)
    print(write_to_file(file_name="./data_file.txt", text=new_event.__repr__()))


def read_events():
    reading_type = input("Вывод события/событий:\nall - всех событий\none - конкретное событие\n")
    if reading_type == "all":
        reading_all()
    elif reading_type == "one":
        reading_one()


def start_runner():
    while True:
        print("Введите команду\n1 - Добавить событие\n2 - Вывод событий\n")
        command = input()
        if command == "1":
            add_event()
        elif command == "2":
            read_events()