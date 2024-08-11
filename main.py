from Models.Product import Product
from Helpers.ProductHelper import ProductHelper

item1 = Product
item2 = Product("Computer")
item3 = Product("Computer", 750)
item4 = Product("Computer", 750, 3)

product_list = ProductHelper.create_item_from_text()

total_balance = ProductHelper.get_total_balance(product_list)

print(total_balance)
