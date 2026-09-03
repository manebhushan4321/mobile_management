# ==========================================
# Mobile Store Management System
# File : products.py
# ==========================================

from db import connect_db, close_db


def product_menu():

    while True:

        print("\n" + "=" * 50)
        print("       PRODUCT MANAGEMENT")
        print("=" * 50)

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")



def add_product():

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        print("\n========== ADD PRODUCT ==========\n")

        brand = input("Brand : ")
        model = input("Model : ")
        ram = input("RAM : ")
        storage = input("Storage : ")
        processor = input("Processor : ")
        display = input("Display : ")
        battery = input("Battery : ")
        camera = input("Camera : ")
        color = input("Color : ")
        price = float(input("Price : "))
        stock = int(input("Stock : "))
        category_id = int(input("Category ID : "))


        query = """
        INSERT INTO products
        (brand, model, ram, storage, processor, display,
        battery, camera, color, price, stock, category_id)

        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """


        values = (
            brand,
            model,
            ram,
            storage,
            processor,
            display,
            battery,
            camera,
            color,
            price,
            stock,
            category_id
        )


        cursor.execute(query, values)
        connection.commit()

        print("\nProduct Added Successfully")


    except Exception as e:
        print("Error :", e)


    finally:
        cursor.close()
        close_db(connection)




def view_products():

    connection = connect_db()

    if connection is None:
        return


    cursor = connection.cursor()


    query = """
    SELECT p.product_id,
           p.brand,
           p.model,
           p.ram,
           p.storage,
           p.processor,
           p.display,
           p.battery,
           p.camera,
           p.color,
           p.price,
           p.stock,
           c.category_name

    FROM products p

    JOIN categories c
    ON p.category_id = c.category_id
    """


    cursor.execute(query)

    products = cursor.fetchall()


    if not products:

        print("\nNo Products Found")


    else:

        print("\n========== PRODUCT LIST ==========")


        for p in products:

            print("\nProduct ID :", p[0])
            print("Brand      :", p[1])
            print("Model      :", p[2])
            print("RAM        :", p[3])
            print("Storage    :", p[4])
            print("Processor  :", p[5])
            print("Display    :", p[6])
            print("Battery    :", p[7])
            print("Camera     :", p[8])
            print("Color      :", p[9])
            print("Price      :", p[10])
            print("Stock      :", p[11])
            print("Category   :", p[12])
            print("-"*40)


    cursor.close()
    close_db(connection)




def search_product():

    connection = connect_db()

    if connection is None:
        return


    cursor = connection.cursor()


    model = input("\nEnter Product Model : ")


    query = """
    SELECT p.product_id,
           p.brand,
           p.model,
           p.ram,
           p.storage,
           p.processor,
           p.display,
           p.battery,
           p.camera,
           p.color,
           p.price,
           p.stock,
           c.category_name

    FROM products p

    JOIN categories c
    ON p.category_id = c.category_id

    WHERE p.model=%s
    """


    cursor.execute(query,(model,))

    product = cursor.fetchone()


    if product:

        print("\n========== PRODUCT DETAILS ==========")

        for data in product:
            print(data)

    else:

        print("\nProduct Not Found")


    cursor.close()
    close_db(connection)




def update_product():

    view_products()


    connection = connect_db()

    if connection is None:
        return


    cursor = connection.cursor()


    product_id = int(input("\nEnter Product ID : "))


    brand = input("Brand : ")
    model = input("Model : ")
    ram = input("RAM : ")
    storage = input("Storage : ")
    processor = input("Processor : ")
    display = input("Display : ")
    battery = input("Battery : ")
    camera = input("Camera : ")
    color = input("Color : ")
    price = float(input("Price : "))
    stock = int(input("Stock : "))
    category_id = int(input("Category ID : "))


    query = """
    UPDATE products

    SET brand=%s,
    model=%s,
    ram=%s,
    storage=%s,
    processor=%s,
    display=%s,
    battery=%s,
    camera=%s,
    color=%s,
    price=%s,
    stock=%s,
    category_id=%s

    WHERE product_id=%s
    """


    values = (
        brand,
        model,
        ram,
        storage,
        processor,
        display,
        battery,
        camera,
        color,
        price,
        stock,
        category_id,
        product_id
    )


    try:

        cursor.execute(query,values)
        connection.commit()

        print("\nProduct Updated Successfully")


    except Exception as e:

        print("Error :",e)


    finally:

        cursor.close()
        close_db(connection)




def delete_product():

    view_products()

    connection = connect_db()

    if connection is None:
        return


    cursor = connection.cursor()


    product_id = int(input("\nEnter Product ID : "))


    query = """
    DELETE FROM products
    WHERE product_id=%s
    """


    try:

        cursor.execute(query,(product_id,))
        connection.commit()

        print("\nProduct Deleted Successfully")


    except Exception as e:

        print("Error :",e)


    finally:

        cursor.close()
        close_db(connection)