from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """Создание экземпляра дочернего класса phone,
           от родительского класса item.
           :param name: Название телефона.
           :param price: Цена за единицу товара.
           :param quantity: Количество товара в магазине.
           :param sim: Количество сим кард в телефоне.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Вывод информации об откладки для разрабочика"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        """Вывод инфонрмации для пользователя"""
        return f'{self.name}'

    def __add__(self, other):
        """Функция провереряет обьекты и складывает кол-во товаров"""
        if not isinstance(other, Item):
            raise ValueError('Склыдывать можно только обьекты Item или из дочерних классов')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.__number_of_sim = int(number)
