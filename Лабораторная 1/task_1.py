import doctest


class Chocolate:
    def __init__(self, weight_of_chocolate: int, energy_value: int):
        """
        Создание и подготовка к работе объекта "Шоколад"
        :param weight_of_chocolate: Масса шоколада
        :param energy_value: Энергетическая ценность
        """
        self.weight_of_chocolate = weight_of_chocolate
        self.energy_value = energy_value

    def is_chocolate(self) -> bool:
        """
        Функция которая проверяет является ли словарь шоколадкой
        :return: Является ли объект шоколадкой или нет
        """
        ...

    def add_nuts_to_chocolate(self, nuts: int) -> int:
        """
        Добавление орехов в шоколад.
        Если количество орехов превышает доступное место,
        то возвращается количество непоместившихся орехов
        :param nuts: Объем добавляемых орехов
        :return: Объем непоместившихся орехов
        """
        ...

    def share_chocolate(self, amount_remaining_chocolate: int) -> int:
        """
        Делимся шоколадкой с друзьями
        Если количество отданного шоколада превышает количество шоколада в упаковке,
        то возвращается реальное количество отданного шоколада
        :param amount_remaining_chocolate: Масса отданного шоколада
        :return: Масса реально отданного шоколада
        """
        ...


if __name__ == "__main__":
    chocolate = Chocolate(80, 1230)  # инициализация экземпляра класса
    doctest.testmod()


class Sofa:
    def __init__(self, height: int, occupied_area: int):
        """
        Создание и подготовка к работе объекта "Диван"
        :param height: Высота
        :param occupied_area: Занимаемая площадь
        """
        self.height = height
        self.occupied_area = occupied_area

    def is_sofa(self) -> bool:
        """
        Функция которая проверяет является ли словарь диваном
        :return: Является ли объект диваном или нет
        """
        ...

    def sofa_upholstery(self, cloth: int) -> int:
        """
        Обиваем диван тканью.
        Если количество имеющейся ткани превышает необходимое,
        то возвращается количество оставшейся ткани
        :param cloth: Нужное количество ткани
        :return: Оставшееся количество ткани
        """
        ...

    def placing_friends_on_sofa(self, friends: int) -> int:
        """
        Размещение друзей на диване
        Если количество друзей в квартире превышает количество друзей на диване,
        то возвращается количество друзей, которым не хватило места на диване.
        :param friends: Количество друзей на диване
        :return: Количество друзей, которым не хватило места
        """
        ...


if __name__ == "__main__":
    sofa = Sofa(42, 23)  # инициализация экземпляра класса
    doctest.testmod()


class Phone:
    def __init__(self, price: int, memory_capacity: int):
        """
        Создание и подготовка к работе объекта "Телефон"
        :param price: Цена телефона
        :param memory_capacity: Объем памяти
        """
        self.price = price
        self.memory_capacity = memory_capacity

    def is_phone(self) -> bool:
        """
        Функция которая проверяет является ли словарь телефоном
        :return: Является ли объект телефоном или нет
        """
        ...

    def payment_subscription_fee(self, subscription_fee: int) -> int:
        """
        Оплачиваю абонентскую плату.
        Если количество имеющихся денег превышает абонентскую плату,
        то возвращается количество оставшихся денег.
        :param subscription_fee: Стоимость адонентской платы за месяц
        :return: Количество оставшихся денег у вас в кошельке
        """
        ...

    def service_life(self, phone_service_life: int) -> int:
        """
        Срок эксплуатации.
        Если срок работы телефона превышает срок эксплуатации телефона по указанной в инструкции,
        то возвращается реальный срок эксплуатации телефона
        :param phone_service_life: Срок эксплуатации телефона
        :return: Срок реальной эксплуатации телефона
        """
        ...


if __name__ == "__main__":
    phone = Phone(50000, 256)  # инициализация экземпляра класса
    doctest.testmod()
