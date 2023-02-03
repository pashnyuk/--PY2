class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга: {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError(f"error count of pages")
        else:
            raise AttributeError(f"error type of pages")

    def __str__(self):
        return f"Книга: {self.name}. Автор {self.author}. Количество страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        if isinstance(duration, float):
            super().__init__(name, author)
            if duration > 0:
                self.duration = duration
            else:
                raise AttributeError(f"error tine of duration")
        else:
            raise AttributeError(f"error type")

    def __str__(self):
        return f"Книга: {self.name}. Автор {self.author}. Продолжительность: {self.duration}"


Book_1 = Book("Женское счастье", "Эмиль Золя")
print(Book_1)
Book_2 = PaperBook("Важные годы", "Мэг Джей", 387)
print(Book_2)
Book_3 = AudioBook("Дом кривых стен", "Содзи Симада", 271.8)
print(Book_3)
