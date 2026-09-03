# ==========================================
# Mobile Store Management System
# File : main.py
# ==========================================

from auth import admin_login
from products import product_menu
from categories import category_menu
from cart import cart_menu
from orders import order_menu
from payments import payment_menu


def main():

    while True:

        print("\n" + "=" * 50)
        print("      MOBILE STORE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Admin Login")
        print("2. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            login = admin_login()

            if login:
                print("\nLogin Successful.")
                admin_menu()

            else:
                print("\nInvalid Username or Password.")

        elif choice == "2":

            print("\nThank You.")
            break

        else:

            print("\nInvalid Choice")


def admin_menu():

    while True:

        print("\n" + "=" * 50)
        print("             ADMIN PANEL")
        print("=" * 50)

        print("1. Product Management")
        print("2. Category Management")
        print("3. Cart Management")
        print("4. Order Management")
        print("5. Payment Management")
        print("6. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            product_menu()

        elif choice == "2":

            category_menu()

        elif choice == "3":

            cart_menu()

        elif choice == "4":

            order_menu()

        elif choice == "5":

            payment_menu()

        elif choice == "6":

            print("\nLogged Out.")
            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":

    main()