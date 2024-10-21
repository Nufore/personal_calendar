from models.event import Event


def create_event(date, time, category: str, title: str, description:str) -> Event:
    new_event = Event(
        date=date,
        time=time,
        category=category,
        title=title,
        description=description,
    )

    return new_event
