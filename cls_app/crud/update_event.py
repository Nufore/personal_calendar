

def get_id_to_update_event(id_line_list):
    print("Какое событие редактировать?")
    for data in id_line_list:
        print(f"{data[0]} - {data[1][:-1]}")
    event_id = int(input())
    if event_id in [data[0] for data in id_line_list]:
        return event_id
    else:
        print("Введите id из представленного списка выше")
        return get_id_to_update_event(id_line_list)

