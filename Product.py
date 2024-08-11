import datetime

class Product(object):

    def __init__(self, name = "Default", price = 0, quantity = 1):
        self.__name = None
        self.__price = None
        self.__quantity = None

        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)

        print(f"{self.__name} {datetime.date.today()}")

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity

    def set_name(self, value):
        if len(value) >= 3 and len(value) <= 8:
            self.__name = value
        else:
            raise ValueError("Name must be between 3 and 8 characters.")
    def set_price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price value must be at least 0.")
    def set_quantity(self, value):
        if value >= 1:
            self.__quantity = value
        else:
            raise ValueError("Quantity value must be at least 1.")
    def get_total_price(self):
        return self.__price * self.__quantity

    def __repr__(self):
        return f"{self.__name} - {self.__price} - {self.__quantity}"