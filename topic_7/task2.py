class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"«{self.title}», {self.author}, {self.pages} с."

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return (self.title, self.author) == (other.title, other.author)

    def __lt__(self, other):
        return self.pages < other.pages

    def __add__(self, other):
        return self.pages + other.pages


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    book1 = Book("Книга1", "Автор1", 320)
    book2 = Book("Книга2", "Автор2", 160)
    book3 = Book("Книга1", "Автор1", 400)

    print("__init__ + __str__ :", book1)
    print("__repr__           :", repr(book1))
    print("список (через __repr__):", [book1, book2])
    print("__len__            :", len(book1))
    print("__eq__ (1 == 3)    :", book1 == book3)
    print("__eq__ (1 == 2)    :", book1 == book2)
    print("__lt__ (2 < 1)     :", book2 < book1)
    print("__add__ (1 + 2)    :", book1 + book2)
    print("sorted за __lt__   :", sorted([book1, book2]))

    point = Point(1, 2)
    print("Без __str__        :", point)

main()
