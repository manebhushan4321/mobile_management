# ==========================================
# Mobile Store Management System
# File : auth.py
# Purpose : Admin Authentication
# ==========================================

from db import connect_db, close_db


def admin_login():

    connection = connect_db()

    if connection is None:
        print("Database Connection Failed!")
        return False

    cursor = connection.cursor()

    print("\n========== ADMIN LOGIN ==========\n")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    query = """
    SELECT *
    FROM admins
    WHERE username=%s
    AND password=%s
    """

    values = (username, password)

    cursor.execute(query, values)

    admin = cursor.fetchone()

    cursor.close()
    close_db(connection)

    if admin:
        print("\n✅ Login Successful")
        return True

    else:
        print("\n❌ Invalid Username or Password")
        return False