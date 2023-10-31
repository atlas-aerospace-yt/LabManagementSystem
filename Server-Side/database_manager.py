"""
This file contains the DatabaseManager class.
"""

import sqlite3

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
