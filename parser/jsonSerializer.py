from json import JSONEncoder
from typing import Any
from item import Item
from datetime import datetime


class itemEncoder(JSONEncoder):
    def default(self, o: Item or datetime or set) -> Any:
        if type(o) == datetime:
            return o.strftime("%a, %d %b %Y %H:%M:%S %z")
        if isinstance(o, set):
            return list(o)
        return o.__dict__


