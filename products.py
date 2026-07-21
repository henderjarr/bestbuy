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
        """returns the quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """sets the quantity of the product, if the quantity is less than or equal to 0, the product is deactivated"""
        self.quantity = quantity
        if quantity <= 0:
            self.deactivate()

    def is_active(self):
        """returns whether the product is active or not"""
        return self.active

    def activate(self):
        """activates the product"""
        self.active = True

    def deactivate(self):
        """deactivates the product"""
        self.active = False

    def show(self):
        """prints the product's name, price, and quantity"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """buys a quantity and sets the new quantity of the product, checks to make sure there is enough quantity available, returns the total price of the purchase"""
        if quantity > self.quantity:
            raise ValueError("not enough quantity available")
        self.set_quantity(self.quantity - quantity)

        total_price = self.price * quantity
        return total_price
