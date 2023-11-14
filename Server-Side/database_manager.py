"""
This file contains the DatabaseManager class.

Documentation of sqlite3: https://docs.python.org/3/library/sqlite3.html
https://stackoverflow.com/questions/36243538/python-sqlite3-how-often-do-i-have-to-commit
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

        self.cursor.execute(sql.CREATE_LABS_TABLE)
        self.cursor.execute(sql.CREATE_USERS_TABLE)
        self.cursor.execute(sql.CREATE_SUPPLIER_TABLE)
        self.cursor.execute(sql.CREATE_STOCK_TABLE)
        self.cursor.execute(sql.CREATE_BOOKINGS_TABLE)
        self.cursor.execute(sql.CREATE_BOOKED_STOCK_TABLE)

        # The only unlinked table
        self.cursor.execute(sql.CREATE_INSTITUTION_TABLE)
        if not self.send_command("SELECT * FROM INSTITUTION"):
            print("triggered")
            self.cursor.execute(sql.INSERT_DEFAULT_PASSWORD)

    def send_command(self, command:str)-> list:
        """
        This relays the SQL command to the database. The try except is needed incase
        the admins enter any incorrect commands.

        Args:
            command(str) : the SQL command that is to be run
        
        Returns:
            str: the result from the sql command.
        """
        try:
            self.cursor.execute(command)
            output = self.cursor.fetchall()
            self.connection.commit()
        except sqlite3.Error as error:
            output = [str(error)]

        return output

    def end_connection(self):
        """
        This closes the connection between the server and the database
        and commits any unsaved data.
        """

        self.cursor.close()
        self.connection.commit()
        self.connection.close()

# If the file is run on its own, it fills the database with testing data
# this if for development and should not affect end users.
if __name__ == "__main__":

    # Get the SQL definitions for test data.
    import Definitions.testing_definitions as test

    print("Filling in the tables.")

    my_database = DatabaseManager()

    # Fill in the database with test data.
    for query in test.FILL_USERS:
        print(my_database.send_command(query))
    for query in test.FILL_LABS:
        print(my_database.send_command(query))
    for query in test.FILL_SUPPLIER:
        print(my_database.send_command(query))
    for query in test.FILL_STOCK:
        print(my_database.send_command(query))
    for query in test.FILL_BOOKINGS:
        print(my_database.send_command(query))
    for query in test.FILL_BOOKED_STOCK:
        print(my_database.send_command(query))

    # Show the user that the data has been entered.
    print(my_database.send_command("SELECT * FROM USERS"))
    print(my_database.send_command("SELECT * FROM LABS"))
    print(my_database.send_command("SELECT * FROM SUPPLIER"))
    print(my_database.send_command("SELECT * FROM STOCK"))
    print(my_database.send_command("SELECT * FROM BOOKINGS"))
    print(my_database.send_command("SELECT * FROM BOOKED_STOCK"))
    print(my_database.send_command("SELECT * FROM INSTITUTION"))

    my_database.end_connection()
