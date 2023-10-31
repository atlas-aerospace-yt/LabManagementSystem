"""
This file contains the DatabaseManager class.

Documentation of sqlite3: https://docs.python.org/3/library/sqlite3.html
"""

import sqlite3

CREATE_SUPPLIER_TABLE = """CREATE TABLE IF NOT EXISTS SUPPLIER
(
SupplierID INTEGER PRIMARY KEY,
Name VARCHAR(100),
);"""

CREATE_STOCK_TABLE = """CREATE TABLE IF NOT EXISTS STOCK
(
    
);"""

CREATE_BOOKED_STOCK_TABLE = """CREATE TABLE IF NOT EXISTS BOOKED_STOCK
(
    
);"""

CREATE_BOOKING_TABLE = """CREATE TABLE IF NOT EXISTS BOOKING
(
    
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS USERS
(
    
);"""

CREATE_LABS_TABLE = """CREATE TABLE IF NOT EXISTS LABS
(
    
);"""


class DatabaseManager:
    """
    The database manager class handles communication with the
    database.
    """

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    def send_command(self, command:str)-> str:
        """
        This relays the SQL command to the database

        Args:
            command(str) : the SQL command that is to be run
        
        Returns:
            str: the result from the sql command.
        """

        self.cursor.execute(command)
        self.cursor.commit()
        return self.cursor.fetchall

    def end_connection(self):
        """
        This closes the connection between the server and the database.
        """

        self.cursor.close()
        self.connection.close()
