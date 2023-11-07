"""
This file contains the DatabaseManager class.

Documentation of sqlite3: https://docs.python.org/3/library/sqlite3.html
"""

import sqlite3
import Definitions.sql_definitions as sql

class DatabaseManager:
    """
    The database manager class handles communication with the
    database.
    """

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        # Create the database tables if they do not already exist
        self.cursor.execute(sql.CREATE_LABS_TABLE)
        self.cursor.execute(sql.CREATE_USERS_TABLE)
        self.cursor.execute(sql.CREATE_SUPPLIER_TABLE)
        self.cursor.execute(sql.CREATE_STOCK_TABLE)
        self.cursor.execute(sql.CREATE_BOOKINGS_TABLE)
        self.cursor.execute(sql.CREATE_BOOKED_STOCK_TABLE)

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
            output = self.cursor.fetchall()
        except sqlite3.Error as error:
            output = [str(error)]

        return output

    def end_connection(self):
        """
        This closes the connection between the server and the database.
        """

        self.cursor.close()
        self.connection.commit()
        self.connection.close()
