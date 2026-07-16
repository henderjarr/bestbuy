class Store:
    """class to represent a store that contains products"""

    def __init__(self, products):
        """initializes the store with a list of products"""
        self.products = products

    def add_product(self, product):
        """adds a product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """removes a product from the store"""
        self.products.remove(product)

    def get_total_quantity(self):
        """returns the total quantity of all products in the store"""
        total = 0
        for product in self.products:
            quant = product.get_quantity()
            total += quant
        return total

    def get_all_products(self):
        """returns a list of all active products in the store"""
        all_prod = []
        for product in self.products:
            if product.is_active():
                all_prod.append(product)
        return all_prod

    def order(self, shopping_list):
        """processes an order for a list of products and quantities"""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
