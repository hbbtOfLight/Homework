class Pagination:

    def __init__(self, text: str, count):
        self.text = text
        self.pages = list()
        self.count = count
        curr = 0
        while curr < len(text):
            self.pages.append(text[curr:curr + count])
            curr += count

    def page_count(self):
        return len(self.pages)

    def item_count(self):
        return len(self.text)

    def item_count_on_page(self, idx):
        if idx >= len(self.pages):
            raise IndexError("Invalid index. Page is missing.")
        return len(self.pages[idx])

    def display_page(self, idx):
        return self.pages[idx]

    def find_pages(self, s: str):
        curr = 0
        found_pages = set()
        while curr < self.item_count():
            curr = self.text.find(s, curr)
            if curr == -1:
                return list(found_pages)
            first = curr//self.count
            width = curr % self.count + len(s)
            width = width // self.count + int(width % self.count != 0)
            for i in range(width):
                found_pages.add(first + i)
            curr += 1
        return list(found_pages)


pages = Pagination('aaaaaaaaaa', 5)
print(pages.page_count())
print(pages.item_count())
print(pages.display_page(0))
print(pages.find_pages("aaaaa"))
print(pages.find_pages("a"))
print(pages.find_pages("aaaaqq"))
