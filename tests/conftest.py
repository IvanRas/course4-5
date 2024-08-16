import pytest

from src.main import Category, Product


@pytest.fixture
def samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни",
                    1)


@pytest.fixture
def prise():
    return 180000.0


@pytest.fixture
def new_product():
    return (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 руб. Остаток: 8 шт.Xiaomi Redmi "
        "Note 11, 31000.0 руб. Остаток: 14 шт.")

