from collections import deque


class CustomDict:
    def __init__(self, map):
        self.map = map
        self.history = deque([None] * 10)

    def set_val(self, key, val):
        if key not in self.map or self.map[key] != val:
            self.history.append(key)
            self.history.popleft()
            self.map[key] = val

    def get_history(self):
        return self.history

    def get_val(self, val):
        return self.map[val]


my_dict = CustomDict({"123": 2, "124": 5, 3: "d"})
my_dict.set_val(1, 2)
my_dict.set_val(3, 2)
my_dict.set_val("No rest for the wicked", "Panic!")
my_dict.set_val("No est for the wicked", "Panic!")
my_dict.set_val("No rest or the wicked", "Panic!")
my_dict.set_val("No rest for the widked", "Panic!")
my_dict.set_val("No rest for the iched", "Panic!")
my_dict.set_val("Rest for the wicked", "Panic!")
my_dict.set_val("No rest for te wicked", "Panic!")
my_dict.set_val("No rest for the vic", "Panic!")
my_dict.set_val("for the wicked", "Panic!")
print(my_dict.get_history())
print(my_dict.get_val(100))
