import time as tm
import os,random,base64
print("\t--------------------------------------")
print("\t \tBakery Management System")
print("\t--------------------------------------")

# For Admin MENU
def admin_menu():
    while True:
        print("This features will be added when i am done with django . FOr now enjoy Ezploiting BUg's")
        print("Flag ain't here !!!")
# Countdown and Clear screen  for Menu and ADmin Section.
def clear_screen():
   os.system('cls' if os.name=='nt' else 'clear')
# For Inuput checking
def input_done():
    return input if input.strip() else None
# For timeout
def countdown_timer(seconds):
    for remaining in range(seconds,0,-1):
        clear_screen()

        print(f"Sorry! Try again after {remaining} seconds.")
        print("Enter 'm' to go back to menu or 'q' to quit.")
        tm.sleep(1)
        if input_done():
            return
    clear_screen()
    print("You can now try again.")
# Current Product list
products = {
    1: {"name": "Bread", "price": 20},
    2: {"name": "Cake wala Bread", "price": 30},
    3: {"name": "Cookie", "price": 100},
}
customer_cart = {}
# Customer Section
def view_product():
    print("-------------------\n")
    print("Available Products\n")
    print("{:<5} {:<10} {:<15}".format("ID", "Product", "Price"))
    print("-----------------------------")
    for prod_id, details in products.items():
        print("{:<5} {:<15} {:<10}\n".format(prod_id, details["name"], details["price"]))
# Order placement customer
def place_order():
    view_product()
    while True:
        prodnum = input("Enter the product number to enter in cart (or q to return  back): ")
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
            print("Invalid product ID. Please choose a product from 1 to 3.")
# Checking Cart
def check_cart():
    clear_screen()
    if customer_cart:
        print("-------------------\n")
        print("Your Cart:")
        print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Product", "Price", "Quantity"))
        for prod_id, details in customer_cart.items():
            print(
                "{:<5} {:<15} {:<10} {:<10}\n".format(
                    prod_id, details["name"], details["price"], details["quantity"]
                )
            )
    else:
        print("Your cart is empty.")

def a1(data, key):
    return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
def b1():
    r_key = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(8))
    return r_key
def c1(s):
    encoded = base64.b64encode(s.encode("utf-8"))
    return encoded
def d1(encoded):
    decoded = base64.b64decode(encoded).decode("utf-8")
    return decoded
def e1():
    print("LOLIPOP!")


def f1():
    g1 = a1("flag{decoy_1}", "decoy_key")
    g2 = a1("flag{decoy_2}", "another_decoy")

    h1 = a1("fl", b1())
    h2 = a1("ag{y", b1())
    h3 = a1("oHON", b1())
    h4 = a1("Etari", b1())
    h5 = a1("ka}", b1())

    final_encoded = h1 + h2 + h3 + h4 + h5
    encoded_flag = a1(final_encoded, "key123")
    w1 = a1(encoded_flag, "key123")
    if random.choice([True, False]):
        print(f"[REAL FLAG] Jhanda: {w1}")
    else:
        print(f"[LOLIPOP] Jhanda: {g1}")


def pay_ment(total_cost):
    print("\nLet's Pay...\n")
    b_size = 10
    print(f"Total is {total_cost}. Enter the amount: ")

    paid_amt = input()
    try:
        paid_amt_value = float(paid_amt[:b_size])
    except ValueError:
        print("Invalid amount!")
        return

    if paid_amt_value < total_cost:
        print(f"You need to pay {total_cost - paid_amt_value} more.")
        anom = input("Want to remove items from the cart? (y/n): ").lower()
        if anom == "y":
            print("Don't give us too much trouble. Earn more, DUDE...")
            return
        else:
            print("Another Way MAYBE.")
    else:
        change = paid_amt_value - total_cost
        print(f"Payment successful! Your change is {change}.\n")
        if len(paid_amt) > b_size:
            print("[Overflow Detected] What are you doing??...")
            if change == 0:
                e1()
            elif change > 0 and any(c.isalpha() for c in paid_amt):
                print("..................")
                tm.sleep(3)
                if "x" in paid_amt and len(paid_amt) > b_size + 5:
                    f1()
                else:
                    e1()
            else:
                print("LOLIPOP.")
        else:
            print("Thank you!! Come back again!")

# Customer Menu
def customer_menu():
    while True:
        print("\t--------------------------------------")
        print("\t\tOptions")
        print("\t--------------------------------------")
        print("1. View Products")
        print("2. Place an Order")
        print("3. Check Cart")
        print("4. CheckOut")
        print("5. Retrun to home")
        print("6. Exit the BMS")

        choiceforcus = input("Enter your Choice(1-6): ")
        if choiceforcus.isdigit() and int(choiceforcus) in range(1, 7):
            choiceforcus = int(choiceforcus)
            if choiceforcus == 1:
                clear_screen()
                view_product()
            elif choiceforcus == 2:
                clear_screen()
                place_order()
            elif choiceforcus == 3:
                check_cart()
            elif choiceforcus ==4:
                pay_ment(calculate_total_cost())
            elif choiceforcus==5:
                clear_screen()
                bms.role_selection()    
            elif choiceforcus == 6:
                print("Exiting...")
                break

class BakeryMgmtSys:
    def __init__(self):
        self.a = False  
        self.b = random.randint(15, 25)  
        self.c = "admin" 
        self.d = "password123"  

    def role_selection(self):
        print("Welcome to Vulnerable BMS \n")
        print("Are you an Admin or a Customer?")
        print("1. Admin")
        print("2. Customer")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Please Verify that you are an Admin.\n")
            self.verify_admin()
    def verify_admin(self):
        x = input("Enter your username: ")
        if len(x) > self.b:
            self.rop_attack()
            return
        y = input("Enter your password: ")
        if x == self.c and y == self.d:
            print("Welcome Admin.")
            self.a = True
        else:
            print("LOLLIPOP.")

    def rop_attack(self):
        print(" ROP.")
        self.a = True
        print("Congrats")

if __name__ == "__main__":
    bms = BakeryMgmtSys()
    bms.role_selection()
def calculate_total_cost():
    total = 0
    for item in customer_cart.values():
        total += item["price"] * item["quantity"]
    return total

