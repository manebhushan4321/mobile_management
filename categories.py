# ==========================================
# Mobile Store Management System
# File : categories.py
# ==========================================

from db import connect_db, close_db


def category_menu():

    while True:

        print("\n" + "=" * 50)
        print("      CATEGORY MANAGEMENT")
        print("=" * 50)
        print("1. Add Category")
        print("2. View Categories")
        print("3. Search Category")
        print("4. Update Category")
        print("5. Delete Category")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_category()

        elif choice == "2":
            view_categories()

        elif choice == "3":
            search_category()

        elif choice == "4":
            update_category()

        elif choice == "5":
            delete_category()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")


def add_category():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    category_name = input("Enter Category Name : ")

    query = """
    INSERT INTO categories(category_name)
    VALUES(%s)
    """

    try:
        cursor.execute(query, (category_name,))
        connection.commit()
        print("Category Added Successfully")

    except Exception as e:
        print("Error :", e)

    finally:
        cursor.close()
        close_db(connection)


def view_categories():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    query = "SELECT * FROM categories"

    cursor.execute(query)

    categories = cursor.fetchall()

    print("\nID\tCategory")
    print("-" * 30)

    for category in categories:
        print(category[0], "\t", category[1])

    cursor.close()
    close_db(connection)


def search_category():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    category_name = input("Enter Category Name : ")

    query = """
    SELECT *
    FROM categories
    WHERE category_name=%s
    """

    cursor.execute(query, (category_name,))

    category = cursor.fetchone()

    if category:
        print("\nCategory Found")
        print("ID :", category[0])
        print("Name :", category[1])
    else:
        print("Category Not Found")

    cursor.close()
    close_db(connection)


def update_category():

    view_categories()

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    category_id = input("\nEnter Category ID : ")
    new_name = input("Enter New Category Name : ")

    query = """
    UPDATE categories
    SET category_name=%s
    WHERE category_id=%s
    """

    try:
        cursor.execute(query, (new_name, category_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Category Updated Successfully")
        else:
            print("Category ID Not Found")

    except Exception as e:
        print("Error :", e)

    finally:
        cursor.close()
        close_db(connection)


def delete_category():

    view_categories()

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    category_id = input("\nEnter Category ID : ")

    query = """
    DELETE FROM categories
    WHERE category_id=%s
    """

    try:
        cursor.execute(query, (category_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Category Deleted Successfully")
        else:
            print("Category ID Not Found")

    except Exception as e:
        print("Error :", e)

    finally:
        cursor.close()
        close_db(connection)