# ==========================================
# Mobile Store Management System
# File : payment.py
# ==========================================

from db import connect_db, close_db


def payment_menu():

    while True:

        print("\n" + "=" * 50)
        print("          PAYMENT MANAGEMENT")
        print("=" * 50)

        print("1. Make Payment")
        print("2. View Payments")
        print("3. Update Payment Status")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            make_payment()

        elif choice == "2":
            view_payments()

        elif choice == "3":
            update_payment()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")


def make_payment():

    connection = connect_db()
    cursor = connection.cursor()

    order_id = input("Enter Order ID: ")
    amount = input("Enter Amount: ")
    method = input("Payment Method (Cash/UPI/Card): ")

    query = """
    INSERT INTO payments(order_id, amount, payment_method, status)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(query, (order_id, amount, method, "Paid"))

    connection.commit()

    print("✅ Payment Successful")

    cursor.close()
    close_db(connection)



def view_payments():

    connection = connect_db()
    cursor = connection.cursor()

    query = "SELECT * FROM payments"

    cursor.execute(query)

    payments = cursor.fetchall()

    print("\n----- PAYMENT DETAILS -----")

    for payment in payments:
        print(payment)

    cursor.close()
    close_db(connection)



def update_payment():

    connection = connect_db()
    cursor = connection.cursor()

    payment_id = input("Enter Payment ID: ")
    status = input("Enter New Status: ")

    query = """
    UPDATE payments
    SET status=%s
    WHERE payment_id=%s
    """

    cursor.execute(query,(status,payment_id))

    connection.commit()

    print("✅ Payment Status Updated")

    cursor.close()
    close_db(connection)