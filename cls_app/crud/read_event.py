from file_manager.reader import read_data_by_date_parameters


def reading_all_daily():
    for event in read_data_by_date_parameters():
        print(event)



def reading_all():
    reading_all_type = input("d - на день\nw - на неделю\nm - на месяц\n")
    if reading_all_type == "d":
        reading_all_daily()
    elif reading_all_type == "w":
        ... # reading_all_weekly()
    elif reading_all_type == "m":
        ... # reading_all_monthly()
    else:
        return reading_all()


def reading_one():
    print("ZAGLUSHKA")
