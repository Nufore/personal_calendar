from models.event import Event
from event_validators.input_and_validate_params import set_date, set_time, set_type, set_title, set_description


def create_event() -> Event:
    event_data = [set_date(), set_time(), set_type(), set_title(), set_description()]
    new_event = Event(*event_data)

    return new_event


