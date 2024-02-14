from src.item import Item


class Mixin:
    __language: str = 'EN'

    def change_lang(self) -> None:
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    @property
    def language(self) -> str:
        return self.__language


class Keyboard(Item, Mixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)
