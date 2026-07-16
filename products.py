class Product:
    """class representing a product in the store"""

    def __init__(self, name, price, quantity, active=True):
        if not name:
            raise ValueError("name cannot be empty")
        if price < 0:
            raise ValueError("price cannot be negative")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(
            f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        # buys a quantity:
        self.quantity = self.get_quantity() - quantity
        # returns the total price of the purchase
        total_price = self.price * quantity
        # updates the quantity of the product
        self.quantity -= quantity

        # should return the total price of the purchase
        return total_price

        # should think of poossible errors that could occur
