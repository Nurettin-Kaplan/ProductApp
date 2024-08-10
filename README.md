# Product App Application Requirements

1. The `Product` class should be modeled with the following fields: `name`, `price`, and `quantity`.

2. Objects should be defined and initialized. When creating an object from the `Product` class, the constructor should be able to be called with different parameters.
```python
    - Product()
    - Product("Computer")
    - Product("Computer", 750)
    - Product("Computer", 750, 3)
```

3. The constructor method should print the name of the created object to the screen and provide the date information.

4. For each product, the `get_total_price()` should be calculated according to the following formula:
$$
    total_{price} = item_{price} * item_{quantity} 
$$

5. The attributes of the `Product` class should be encapsulated.
    1. The product name field (`name`) should have a minimum of 3 and a maximum of 8 characters.
    2. The product price (`price`) value should be a minimum of 0.
    3. The product quantity (`quantity`) value should be a minimum of 1.
---
6. When printing the `Product` class, the method from the base-superclass should be overridden.

7. A `ProductHelper` class should be written to use the `Product` class.
    1. It should have a `static` method named `create_item_from_text` that can read from a `.txt` file.
        - The attributes in the text file should be separated by commas.
        - Each line should be read and converted into a `Product` object.
        - Relevant data type conversions should be defined within this method.
    2. It should have a `static` method named `get_total_balance` that calculates the total payment amount in a product list.
        - This method should iterate through the products in the `Product` list passed as a parameter.
        - Each product's price and quantity should be calculated.
        - A 20% VAT rate should be added to the total balance.
---
8. The generated `Product` class should be placed under the `Models` folder.

9. The generated `ProductHelper` class should be placed under the `Helpers` folder.

10. The classes modeled according to the above statements should be used to read the `Products.txt` file.