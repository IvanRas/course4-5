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
    def price(self, new_prise):
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
    products: str  # список товаров категории

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += 1

    def add_product(self,  product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for i in self.__products:
            product_str += f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт."
        return product_str


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
