import datetime


class Event:
    def __init__(self, date, time, category: str, title: str, description:str) -> None:
        self.date: datetime.date = date
        self.time: datetime.time = time
        self.category: str = category
        self.title: str = title
        self.description: str = description


    def __repr__(self) -> str:
        return (f"{self.date} "
                f"{self.time} | "
                f"{self.category} | "
                f"{self.title.replace("_", " ")} | "
                f"{self.description.replace("_", " ")}")


    def data_to_file(self):
        return f"{self.date} {self.time} {self.category} {self.title} {self.description}"