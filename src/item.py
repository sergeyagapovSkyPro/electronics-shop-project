import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "Файл поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """Вывод информации об откладки для разрабочика"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Вывод инфонрмации для пользователя"""
        return f'{self.name}'

    def __add__(self, other):
        """Функция складывает кол-во товаров"""
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Функция проверяет длинну наименования товаров не более 10 символов"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """Добовление экземпляров класса из csv файла"""
        try:
            cls.all = []
            with open(csv_file, newline='', encoding="windows-1251") as file:
                data = csv.DictReader(file)
                for row in data:
                    cls(str(row['name']), float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {csv_file}")
        except KeyError:
            raise InstantiateCSVError

    @staticmethod
    def string_to_number(str_number):
        """Возвращает число из числа - строки"""
        number = float(str_number)
        return int(number)
