"""
This file contains the DatabaseManager class.

Documentation of sqlite3: https://docs.python.org/3/library/sqlite3.html
"""

import sqlite3

CREATE_SUPPLIER_TABLE = """CREATE TABLE IF NOT EXISTS SUPPLIER
(
SupplierID INTEGER NOT NULL PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Phone VARCHAR(11),
Email VARCHAR(254)
);"""

CREATE_STOCK_TABLE = """CREATE TABLE IF NOT EXISTS STOCK
(
StockID INTEGER NOT NULL PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Amount INTEGER NOT NULL,
Price INTEGER NOT NULL,
Website TEXT,
SupplierID INTEGER,
FOREIGN KEY(SupplierID) REFERENCES SUPPLIER(SupplierID)
);"""

CREATE_BOOKED_STOCK_TABLE = """CREATE TABLE IF NOT EXISTS BOOKED_STOCK
(
BookingID INTEGER,
StockID INTEGER,
Amount INTEGER NOT NULL,
FOREIGN KEY(StockID) REFERENCES STOCK(StockID),
FOREIGN KEY(BookingID) REFERENCES BOOKINGS(BookingID)
);"""

CREATE_BOOKINGS_TABLE = """CREATE TABLE IF NOT EXISTS BOOKINGS
(
BookingID INTEGER NOT NULL PRIMARY KEY,
UserID INTEGER,
LabID INTEGER,
Date DATE NOT NULL,
Time TIME NOT NULL,
FOREIGN KEY(UserID) REFERENCES USERS(UserID),
FOREIGN KEY(LabID) REFERENCES USERS(UserID)
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS USERS
(
UserID INTEGER NOT NULL PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Email VARCHAR(254) NOT NULL,
PasswordHash VARCHAR(255) NOT NULL,
Priority INTEGER NOT NULL
);"""

CREATE_LABS_TABLE = """CREATE TABLE IF NOT EXISTS LABS
(
LabID INTEGER PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Location TEXT
);"""


class DatabaseManager:
    """
    The database manager class handles communication with the
    database.
    """

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        # Create the database tables if they do not already exist
        self.cursor.execute(CREATE_LABS_TABLE)
        self.cursor.execute(CREATE_USERS_TABLE)
        self.cursor.execute(CREATE_SUPPLIER_TABLE)
        self.cursor.execute(CREATE_STOCK_TABLE)
        self.cursor.execute(CREATE_BOOKINGS_TABLE)
        self.cursor.execute(CREATE_BOOKED_STOCK_TABLE)

    def send_command(self, command:str)-> str:
        """
        This relays the SQL command to the database

        Args:
            command(str) : the SQL command that is to be run
        
        Returns:
            str: the result from the sql command.
        """

        # The try except is needed incase the admins enter any incorrect
        # commands
        try:
            print("Running command: " + command)
            self.cursor.execute(command)
            return self.cursor.fetchall()
        except sqlite3.Error as error:
            print("SQL Error:\n" + str(error) + "\n",end="")

        return None

    def end_connection(self):
        """
        This closes the connection between the server and the database.
        """

        self.cursor.close()
        self.connection.commit()
        self.connection.close()
