import pytest

from src.main import Product, Category


def test_product(samsung):  # тест на продукт
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


def test_category(category):
    assert category.name == "Смартфоны"
    # assert category.description == ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
    #                                 "функций для удобства жизни")
    # assert category.products == 1


def test_prise(samsung):
    assert samsung.price == 180000.0


def test_new_product(new_product):  # тест на продукт
    assert new_product == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 руб. Остаток: 8 "
                           "шт.Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.")


