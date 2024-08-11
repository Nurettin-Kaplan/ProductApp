from Product import Product
class ProductHelper(Product):
    @staticmethod
    def create_item_from_text():
        products = []

        with open("Products.txt", "r") as products_file:
            for line in products_file:
                id, name, price, quantity = line.strip().split(", ")

                name = name.strip()
                price = float(price.strip())
                quantity = int(quantity.strip())

                product = Product(name, price, quantity)
                products.append(product)
    @staticmethod
    def get_total_balance():
        pass