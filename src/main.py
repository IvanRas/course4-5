from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class Product(BaseProduct):
    """ Информация о свойтвах продуктах"""
    name: str  # название продукта
    description: str  # описание  продукта
    price: str  # цена  продукта
    quantity: float  # количество продукта

    def __init__(self, name, description, price, quantity):
        super().__init__()
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


class MixinLog(Product):

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.order_log()

    def order_log(self):
        print(f'{self.name, self.description, self.price, self.quantity}')


class MixinLog:

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.order_log()

    def order_log(self):
        print(f'{self.name, self.description, self.price, self.quantity}')


class Smartphone(Product, MixinLog):
# class Smartphone(MixinLog):

    """ Информация о смартфоне """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        efficiency: str  # производительность  смартфона
        model: str  # модель смартфона
        memory: int  # объем встроенной памяти
        color: str  # цвет

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError('Складывать можно только объекты Smartphone')
        return (self.price * self.quantity) + (other.price * other.quantity)
        # return f"{self.name},{self.__price} руб. Остаток: {self.quantity}"


class LawnGrass(Product, MixinLog):
# class LawnGrass(MixinLog):
    """ Информация о Трава газонная """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

        country: str  # страна-производитель
        germination_period: str  # срок прорастания
        color: str  # цвет

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError('Складывать можно только объекты LawnGrass')
        return (self.price * self.quantity) + (other.price * other.quantity)
        # return f"{self.name},{self.__price} руб. Остаток: {self.quantity}"


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

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                         "удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и "
                         "помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

print(LawnGrass.__mro__)
print(Smartphone.__mro__)
