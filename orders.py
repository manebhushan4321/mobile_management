# ==========================================
# Mobile Store Management System
# File : order.py
# ==========================================

from db import connect_db, close_db


def order_menu():

    while True:

        print("\n" + "=" * 50)
        print("          ORDER MANAGEMENT")
        print("=" * 50)

        print("1. Place Order")
        print("2. View Orders")
        print("3. Cancel Order")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            place_order()

        elif choice == "2":
            view_orders()

        elif choice == "3":
            cancel_order()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")


def place_order():

    connection = connect_db()
    cursor = connection.cursor()

    user_id = input("Enter User ID: ")
    product_id = input("Enter Product ID: ")
    quantity = int(input("Enter Quantity: "))

    query = """
    INSERT INTO orders(user_id, product_id, quantity)
    VALUES(%s,%s,%s)
    """

    cursor.execute(query, (user_id, product_id, quantity))

    connection.commit()

    print("✅ Order Placed Successfully")

    cursor.close()
    close_db(connection)



def view_orders():

    connection = connect_db()
    cursor = connection.cursor()

    query = """
    SELECT * FROM orders
    """

    cursor.execute(query)

    orders = cursor.fetchall()

    print("\n----- ORDERS -----")

    for order in orders:
        print(order)

    cursor.close()
    close_db(connection)



def cancel_order():

    connection = connect_db()
    cursor = connection.cursor()

    order_id = input("Enter Order ID to Cancel: ")

    query = """
    DELETE FROM orders
    WHERE order_id=%s
    """

    cursor.execute(query,(order_id,))

    connection.commit()

    print("❌ Order Cancelled")

    cursor.close()
    close_db(connection)