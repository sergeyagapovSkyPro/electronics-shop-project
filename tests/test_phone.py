import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr_str(phone):
    """Проверка repr, str"""
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone(phone):
    """Проверка характиристик товара"""
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_number_of_sim(phone):
    """Проверка кол-во поддерживаемых сим-карт"""
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
        phone.number_of_sim = 0
        phone.number_of_sim = 1.2
