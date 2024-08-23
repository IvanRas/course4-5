class Product:
    """ Информация о свойтвах продуктах"""
    name: str  # название продукта
    description: str  # описание  продукта
    price: str  # цена  продукта
    quantity: float  # количество продукта

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name},{self.__price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, new_product: dict):
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    # доп
    # for name in new_product:      # нужно проити перебором по именам
    #     if name in :              # если имя было в старом списке то
    #         quantity += quantity  # к стараму кол-во добавить новое
    #     else:                     № иначе переити к следующему имени
    #         continue

    @property
    def price(self):
        # return f"{self.name}, {self.description}, {self.price}, {self.quantity}"
        return self.__price

    @price.setter
    def price(self, new_prise: float):
        if new_prise <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_prise


class Category:
    """ Информация о котегориях """

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


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
