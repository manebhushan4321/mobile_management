# ==========================================
# Mobile Store Management System
# File : cart.py
# ==========================================

from db import connect_db, close_db


def cart_menu():

    while True:

        print("\n" + "=" * 50)
        print("          CART MANAGEMENT")
        print("=" * 50)

        print("1. Add To Cart")
        print("2. View Cart")
        print("3. Update Cart")
        print("4. Remove From Cart")
        print("5. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_to_cart()

        elif choice == "2":
            view_cart()

        elif choice == "3":
            update_cart()

        elif choice == "4":
            remove_from_cart()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")


def add_to_cart():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    product_id = input("Enter Product ID : ")
    quantity = input("Enter Quantity : ")

    query = """
    INSERT INTO cart(product_id, quantity)
    VALUES(%s, %s)
    """

    try:
        cursor.execute(query, (product_id, quantity))
        connection.commit()
        print("Product Added To Cart Successfully")

    except Exception as e:
        print("Error :", e)

    finally:
        cursor.close()
        close_db(connection)


def view_cart():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    query = "SELECT * FROM cart"

    cursor.execute(query)

    carts = cursor.fetchall()

    print("\n" + "-" * 40)
    print("Cart ID\tProduct ID\tQuantity")
    print("-" * 40)

    for cart in carts:
        print(f"{cart[0]}\t{cart[1]}\t\t{cart[2]}")

    cursor.close()
    close_db(connection)


def update_cart():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    cart_id = input("Enter Cart ID : ")
    quantity = input("Enter New Quantity : ")

    query = """
    UPDATE cart
    SET quantity = %s
    WHERE cart_id = %s
    """

    try:
        cursor.execute(query, (quantity, cart_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Cart Updated Successfully")
        else:
            print("Cart ID Not Found")

    except Exception as e:
        print("Error :", e)

    finally:
        cursor.close()
        close_db(connection)


def remove_from_cart():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    cart_id = input("Enter Cart ID : ")

    query = """
    DELETE FROM cart
    WHERE cart_id = %s
    """

    try:
        cursor.execute(query, (cart_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Product Removed From Cart")
        else:
            print("Cart ID Not Found")

    except Exception as e:
        print("Error :", e)

    finally:
        cursor.close()
        close_db(connection)