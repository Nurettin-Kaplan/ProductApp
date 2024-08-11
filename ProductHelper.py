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
        return products
    @staticmethod
    def get_total_balance(products):
        total = 0
        for product in products:
            total += product.get_price() * product.get_quantity()

        total_with_vat = total * 1.20
        return total_with_vat