from datetime import datetime


class Item:
    def __init__(self, title, date, links, description=""):
        self.title = title
        self.date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")
        self.links = links
        self.description = description

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)

    def __str__(self):
        return f"Title:{self.title}" + "\n" + f"Date:{self.date}\nLink:{self.links}\nDescription: {self.description}"

    def __repr__(self):
        return self.__str__()
