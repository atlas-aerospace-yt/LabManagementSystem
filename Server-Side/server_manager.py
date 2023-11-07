"""
This file contains the ServerManager class.
"""

from database_manager import DatabaseManager
from connection_manager import ConnectionManager

class ServerManager:
    """
    The server manager class handles all of the admin inputs
    into the application and connects the connection manager
    to the database manager.

    TODO Add SQL commands to database manager

    TODO comment attributes
    TODO comment methods
    """

    def __init__(self):
        self.admin_commands = [] # a 1D list
        self.sql_commands = [] # a 2D list

        self.sql_results = []
        self.admin_commands = []

        self.connection_manager = ConnectionManager()
        self.database_manager = DatabaseManager()

    def enqueue_sql(self, command:list):
        """
        Enque an SQL command which is to be run.
        
        Args:
            command(list): the admin or ip address, the SQL command
        """
        self.sql_commands.append(command)

    def dequeue_admin_sql(self) -> str:
        """
        Deques the SQL formatted result.

        Returns:
            str: The SQL result formatted with HTML
        """

        # Check that there is data to be returned
        if len(self.sql_results) > 0:
            for result in self.sql_results:
                if result[0] == "admin":
                    del self.sql_results[self.sql_results.index(result)]
                    return result[1]

        # Return an empty string if there is nothing to deque
        return ""

    def enqueue_command(self, command:str):
        """
        Enque an admin terminal command.

        Args:
            command (str): the command to be run
        """
        self.admin_commands.append(command)

    def dequeue_command(self) -> str:
        """
        Dequeu

        Returns:
            str: _description_
        """
        if len(self.admin_commands) > 0:
            return self.admin_commands.pop(0)
        return ""

    def parse_database_output(self, output:list) -> str:
        """
        This function processes the output which is returned from the database
        manager so that it is easy to read on screen for the admins.

        Args:
            ouptut(list): the string that has been output by the database manager

        Returns:
            str: the output from the SQL query with \n breaks
        """
        result = ""

        for item in output:
            if item is not None:
                result += str(item) + "\n"

        if not result:
            result = "No data returned!"

        return result

    def main_loop(self):
        """
        This function gets called every frame
        """

        # Remove all disconnected users
        for item in self.connection_manager.connections:
            if item.disconnected is True:
                del self.connection_manager.connections[
                    self.connection_manager.connections.index(item)]
                print(f"Removed: {item.address[0]}:{item.address[1]}")

        # Add connection managers SQL commands
        sql_commands = self.connection_manager.get_all_new_data()
        if sql_commands:
            for command in sql_commands:
                self.enqueue_sql(command)

        # Check if there is an SQL command to run
        if len(self.sql_commands) > 0:
            sql_command = self.sql_commands.pop(0)
            output = self.database_manager.send_command(sql_command[1])
            self.sql_results.append(
                [sql_command[0], f"{sql_command[1]}\n{self.parse_database_output(output)}"])

        # Check if there is an admin command to run
        if len(self.admin_commands) > 0:
            admin_command = self.admin_commands.pop(0)
            # TODO does not do anything yet
            self.admin_commands.append(admin_command)

        # Send the data to the client once it has been processed
        if self.sql_results:
            for result in self.sql_results:
                for connection in self.connection_manager.connections:
                    if connection.address == result[0]:
                        connection.send_data(result[1])
                        del self.sql_results[self.sql_results.index(result)]
                        break
