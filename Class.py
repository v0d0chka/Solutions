class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        total_price = self.calculate_total_price()
        print(f"Товар: {self.name}")
        print(f"Ціна: {self.price} грн")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {total_price} грн")


product1 = Product("Ноутбук", 20000, 3)
product1.display_info()

product2 = Product("Мишка", 500, 10)
product2.display_info()