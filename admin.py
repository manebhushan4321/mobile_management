# ==========================================
# Mobile Store Management System
# File : admin.py
# ==========================================

def admin_dashboard():

    while True:

        print("\n" + "=" * 50)
        print("         ADMIN DASHBOARD")
        print("=" * 50)

        print("1. Category Management")
        print("2. Product Management")
        print("3. User Management")
        print("4. Order Management")
        print("5. Payment Management")
        print("6. Reports")
        print("7. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            print("Category Module")

        elif choice == "2":
            print("Product Module")

        elif choice == "3":
            print("User Module")

        elif choice == "4":
            print("Order Module")

        elif choice == "5":
            print("Payment Module")

        elif choice == "6":
            print("Report Module")

        elif choice == "7":
            print("\nLogged Out Successfully...")
            break

        else:
            print("\nInvalid Choice!")