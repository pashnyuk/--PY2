from typing import Tuple, Any


class ProgrammingLanguages:
    def __init__(self, name: str, typing: str):
        """
        Создание и подготовка к работе объекта "Языки программирования"
        :param name: Название языка программирования
        :param typing: Типизация данных
        """
        self.name = name
        self.typing = typing

    def speed_of_operation(self, speed):
        """
        Рассмотрим скорость работы языков программирования
        """
        return f"Высокая скорость работы: {speed} сек"

    def learning(self) -> str:
        """
        Рассмотрим сложность изучения языков программирования
        """
        return "Прост в изучении"

    def __str__(self) -> str:
        return f"Язык программирования: {self.name}. Типизация: {self.typing}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, typing={self.typing!r})"


class Python(ProgrammingLanguages):
    def speed_of_operation(self, speed) -> tuple[str, Any]:
        return f"Низкая скорость работы: {speed} сек"


class Java(ProgrammingLanguages):
    def learning(self) -> str:
        return "Сложен в изучении"


if __name__ == "__main__":
    python = Python("Python", "Неявная сильная динамическая")
    print(python.__str__())
    print(python.speed_of_operation(71.90), "сек")
    print(python.learning())

    java = Java("Java", "Сильная статическая")
    print(java.__str__())
    print(java.speed_of_operation(1.89), "сек")
    print(java.learning())
pass
