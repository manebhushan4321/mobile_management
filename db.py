# ==========================================
# Mobile Store Management System
# File : db.py
# Purpose : Database Connection
# ==========================================

import mysql.connector
from mysql.connector import Error


def connect_db():
    """
    Create and return MySQL database connection.
    Returns:
        connection object if successful
        None if connection fails
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bhushan12345",
            database="mobile_store"
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"\nDatabase Error : {e}")
        return None


def close_db(connection):
    """
    Close MySQL database connection safely.
    """

    if connection is not None:
        if connection.is_connected():
            connection.close()