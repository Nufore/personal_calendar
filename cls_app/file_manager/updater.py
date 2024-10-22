from crud.create_event import create_event


def update_file_by_line_id(line_id: int):
    with open("./data_file.txt", "r+") as file:
        lines = file.readlines()
        updated_event = create_event()
        lines[line_id] = updated_event.data_to_file() + "\n"


    with open("./data_file.txt", "w") as file:
        file.writelines(lines)
