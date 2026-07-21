from products import Product
from store import Store

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250)
                ]
# create a store with the initial stock
best_buy = Store(product_list)


def start(store):
    """starts the store menu"""
    while True:
        print("Store Menu\n----------\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Exit")

        choice = input("Please choose a number: ")

        if choice == "1":
            products = store.get_all_products()
            print("----------------------------------------------------------")
            for index, product in enumerate(products, start=1):
                print(f"{index}. ", end="")
                product.show()
            print("----------------------------------------------------------")

        elif choice == "2":
            print(f"Total of {store.get_total_quantity()} items in store")

        elif choice == "3":
            products = store.get_all_products()
            print("----------------------------------------------------------")
            for index, product in enumerate(products, start=1):
                print(f"{index}. ", end="")
                product.show()
            print("----------------------------------------------------------")

            print("When you want to finish order, enter empty text.")
            shopping_list = []

            while True:
                choose_product = input(
                    "Which product # do you want? ")
                if choose_product == "":
                    break
                choose_product = int(choose_product)
                quantity = int(input("What amount do you want? "))
                shopping_list.append((products[choose_product - 1], quantity))
                print("Product added to list!")

            total_price = store.order(shopping_list)
            print(f"**************\nOrder made! Total payment: ${total_price}")

        elif choice == "4":
            print("Exiting...")
            break


start(best_buy)
