import pytest

from src.main import Product, Category


def test_product(samsung):  # тест на продукт
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


def test_product_creation():
    # Фикстура для теста
    product_data = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 20
    }

    product = Product.new_product(product_data)

    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.0
    assert product.quantity == 20


def test_product_str_method():
    product = Product("Товар 2", "Описание товара 2", 150.0, 5)
    assert str(product) == "Товар 2,150.0 руб. Остаток: 5"


def test_new_price(samsung):
    samsung.price = -100
    assert samsung.price == 180000.0
    samsung.price = 100
    assert samsung.price == 100
    samsung.price = 1
    assert samsung.price == 1


def test_new_product(new_product):  # тест на продукт
    assert new_product == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 руб. Остаток: 8 "
                           "шт.Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.")


def test_new_product_2():
    name_product = Product.new_product({"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP "
                                                                                           "камера", "price": 180000.0,
                                        "quantity": 5})
    assert name_product.name == "Samsung Galaxy S23 Ultra"
    assert name_product.description == "256GB, Серый цвет, 200MP камера"
    assert name_product.price == 180000.0
    assert name_product.quantity == 5


def test_category_add_product():
    product = Product("Товар 3", "Описание товара 3", 200.0, 2)
    category = Category("Категория 2", "Описание категории 2", [])

    category.add_product(product)

    assert len(category.products.split('\n')) - 1 == 1


def test_category_all_products_count():
    product1 = Product("Iphone 15Pro", "Apple", 120000.0, 7)
    product2 = Product("Galaxy S21", "Samsung", 150000.0, 8)
    category = Category("Смартфоны", "телефоны для свзяи", [product1, product2])

    assert str(category) == "Смартфоны, количество продуктов: 15 шт."


def test_add_product():
    product1 = Product("Товар 3", "Описание товара 3", 200.0, 2)
    product2 = Product("Товар 3", "Описание товара 3", 200.0, 2)
    sum_product = product1 + product2

    assert sum_product == 800.0

