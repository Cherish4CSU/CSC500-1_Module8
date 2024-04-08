class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = float(0.0)
        self.item_quantity = int(0) 
        self.item_description = str()
        self.item_total = round(self.item_price * self.item_quantity, 2)
        
    def print_item_cost(self):
        print(f"{self.item_name.title()}: {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total:.2f}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="3/24/24"):
        self.customer_name = customer_name # Corrected line
        self.current_date = current_date # Corrected line
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def add_item_to_cart(self): 
        print('---------------------------------------------------------------')
        print(f"Online Shopping Cart -- TWO ITEMS MINIMUM -- \n Please Add 2 Items To Start")
        print('---------------------------------------------------------------')
        for i in range(2):
            name = input(f"\nItem #{i + 1} Name: ")
            price = float(input(f"Item # {i + 1} Price: $"))
            qty = int(input(f"Item # {i + 1} Quantity: "))
            description = str(input(f"Item #{i + 1} Description (Brand, Color, etc.): "))

            new_item = ItemToPurchase()
            new_item.item_name = name
            new_item.item_price = price
            new_item.item_quantity = qty
            new_item.item_description = description
            new_item.item_total = round(new_item.item_quantity * new_item.item_price, 2)

            self.cart_items.append(new_item)
            print('\n-------------------------------------')
            print(f"Item #{i + 1} Added to Shopping Cart!")
            new_item.print_item_cost()

        total_cost = self.get_cost_of_cart()
        print('-------------------------------------')
        print(f"Shopping Cart Total: ${total_cost:.2f}")
        print('-------------------------------------\n')
            
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return round(sum(item.item_price * item.item_quantity for item in self.cart_items), 2)

    def print_total(self):
        if not self.cart_items:
            print("*** Nothing Found - Your Shopping Cart is Currently Empty ***\n")
        else:
            print(f'Shopping Cart for {self.customer_name.title()} - {self.current_date}')
            print("---------------------------------------")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.item_name.title()}: {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_total:.2f}")
            print("---------------------------------------")
            print(f"Shopping Cart Total: ${self.get_cost_of_cart():.2f}")
            print("---------------------------------------")

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():
                self.cart_items.remove(item)
                print(f"Item '{item_name.title()}' was removed from cart.")
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, updated_item_name, updated_item_qty):
        for i, existing_item in enumerate(self.cart_items):
            if existing_item.item_name.lower() == updated_item_name.lower():
                existing_item.item_quantity = updated_item_qty
                print(f"Thank you! The Shopping cart quantity for '{updated_item_name.title()}' was modified successfully.")
                return
        print("Item not found in cart. Nothing modified.")

    def print_descriptions(self):
        if not self.cart_items:
            print("*** Nothing Found - Your Shopping Cart is Currently Empty ***\n")
        else:
            print(f"\nShopping Cart for {self.customer_name.title()} - {self.current_date}")
            print("Item Descriptions")
            print("---------------------------------------")
            for item in self.cart_items:
                print(f"{item.item_name.title()}: {item.item_description}")
            print("---------------------------------------\n")

def display_menu(cart):
    while True:
        print("\nOnline Shopping Cart - Main Menu")
        print("-------------------------------------")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        if not cart.cart_items:
            print("\n****UH-OH! YOUR SHOPPING CART IS EMPTY!****")
            emptycartanswer = input("Would you like to add two items to your cart to get started? (y/n)\n")
            if emptycartanswer.lower() == "y":
                choice = "a"
            else:
                choice = input("\nPlease choose a menu option: ").lower()
        else:
            choice = input("\nPlease choose a menu option: ").lower()

        if choice == "q":
            break
        elif choice == "a":
            cart.add_item_to_cart()
        elif choice == "r":
            print("\nCurrent items in cart:")
            cart.print_total()
            item_name = input("Please enter the name of the item to remove: ")
            cart.remove_item(item_name)
        elif choice == "c":
            print("\nCurrent items in cart:")
            cart.print_total()
            item_name = input("Enter the name of the item to change quantity: ")
            new_quantity = int(input("Enter the new quantity: "))
            cart.modify_item(item_name, new_quantity)
        elif choice == "i":
            cart.print_descriptions()
        elif choice == "o":
            cart.print_total()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print('-------------------------------------------------')
    print('Welcome to Your Personal Online Shopping Cart')
    print('-------------------------------------------------\n')
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print('\n----------------------------------------')
    print(f"Customer name: {customer_name.title()}")
    print(f"Today's date: {current_date}")
  
    cart = ShoppingCart(customer_name, current_date) # Corrected line
    display_menu(cart)
