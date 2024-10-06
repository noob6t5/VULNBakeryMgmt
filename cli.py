import time as tm
import os

print("\t--------------------------------------")
print("\t \tBakery Management System")
print("\t--------------------------------------")


# For Admin MENU
def admin_menu():
    while True:
        print("Options")
        print("1. Add or remove Product")
        print("2. View Customer's details")
        print("3. View Sales Details")
        print("4. Export data to Excel")
        print("5. Exit")

# Countdown and Clear screen  for Menu and ADmin Section. 
def clear_screen():
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')

# 
        

products = {
    1: {"name": "Bread", "price": 20},
    2: {"name": "Cake", "price": 150},
    3: {"name": "Cookie", "price": 10},
}

customer_cart = {}


# Customer Section
def view_product():
    print("Available Products\n")
    print("{:<5} {:<10} {:<15}".format("ID", "Product", "Price"))
    print("------------------------------------------")
    for prod_id, details in products.items():
        print("{:<5} {:<15} {:<10}".format(prod_id, details["name"], details["price"]))


def place_order():
    view_product()
    while True:
        prodnum = input("Enter the product number to enter in cart (or q to Quit): ")
        if prodnum.lower() == "q":
            break

        if prodnum.isdigit() and int(prodnum) in products:
            prod_id = int(prodnum)
            quantity = int(
                input(f"Enter the quantity for {products[prod_id]['name']}: ")
            )
            if prod_id in customer_cart:
                customer_cart[prod_id]["quantity"] += quantity
            else:
                customer_cart[prod_id] = {
                    "name": products[prod_id]["name"],
                    "price": products[prod_id]["price"],
                    "quantity": quantity,
                }
            print(f"{quantity} {products[prod_id]['name']} added to cart.")
        else:
            print("Invalid product ID. Please choose a product from 1 to 5.")


def check_cart():
    # Add code to display customer cart (currently missing)
    if customer_cart:
        print("Your Cart:")
        print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Product", "Price", "Quantity"))
        for prod_id, details in customer_cart.items():
            print(
                "{:<5} {:<15} {:<10} {:<10}".format(
                    prod_id, details["name"], details["price"], details["quantity"]
                )
            )
    else:
        print("Your cart is empty.")


# Customer Menu
def customer_menu():
    while True:
        print("\t--------------------------------------")
        print("\t\t\t\t\tOptions")
        print("\t--------------------------------------")
        print("1. View Products")
        print("2. Place an Order")
        print("3. Check Cart")
        print("4. CheckOut")
        print("5. Exit")

        choiceforcus = input("Enter your Choice(1-5): ")
        if choiceforcus.isdigit() and int(choiceforcus) in range(1, 6):
            choiceforcus = int(choiceforcus)

            if choiceforcus == 1:
                view_product()

            elif choiceforcus == 2:
                place_order()

            elif choiceforcus == 3:
                check_cart()

            elif choiceforcus == 5:
                print("Exiting...")
                break


# Role Selection
def role_selection():
    print("Are you an Admin or a Customer?")
    print("1. Admin")
    print("2. Customer")
    choice = input("Enter your choice: ")
    if choice == "1":
        attempts = 2

        while attempts > 0:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username == "test" and password == "password123":
                print("Login Success! Welcome Admin")
                tm.sleep(2)
                admin_menu()
                break
            else:
                attempts -= 1
                print(f"Sorry Wrong password {attempts} attempts remaining!")
                if attempts == 0:
                    print("Sorry !! Try again After 30 Seconds")
                    tm.sleep(30)

    elif choice == "2":
        cusname = input("Enter Your Name: ")
        print("Welcome, " + cusname)
        customer_menu()
    else:
        print("Invalid role Chosen!!")


role_selection()
