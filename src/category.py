from src.product import Product


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
