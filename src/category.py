from src.product import Product


class AveragePrice(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class ThereIsNoProduct(AveragePrice):
    """Класс исключения при отсутствии товара """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Товар отсутвует.'


class IncorrectAmount(AveragePrice):
    """Класс исключения при отсутствии товара """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ''


class Category:
    """Информация о котегориях"""

    category_count = 0
    product_count = 0

    name: str  # название продукта
    description: str  # описание продукта
    products: list  # список товаров категории

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        product_str = ""
        for i in self.__products:
            product_str += f"{str(i)}\n"
        return product_str

    def average_price(self, product: Product):
        try:
            for i in self.__products:
                total_price = i * product.quantity
            av_price = total_price / Category.product_count
            return f"cредний ценник всех товаров:{av_price}"
        except ZeroDivisionError:
            print("Ошибка: сумма товаров делиться на ноль")
        except ThereIsNoProduct:
            print("В категории нет товаров")
