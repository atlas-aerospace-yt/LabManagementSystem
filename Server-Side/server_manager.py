"""
This file contains the ServerManager class.
"""

import hashlib

from database_manager import DatabaseManager
from connection_manager import ConnectionManager
from email_manager import EmailManager

EMAIL_CHECK_FREQ = 50

class ServerManager:
    """
    The server manager class handles all of the admin inputs
    into the application and connects the connection manager
    to the database manager.
    """

    def __init__(self):
        self.counter = -1

        self.sql_commands = []
        self.sql_results = []

        self.connection_manager = ConnectionManager()
        self.database_manager = DatabaseManager()
        self.email_manager = EmailManager(self.database_manager)

    def enqueue_sql(self, command:list):
        """
        Enque an SQL command which is to be run.
        
        Args:
            command(list): the admin or ip address, the SQL command
        """
        self.sql_commands.append(command)

    def dequeue_sql(self) -> list:
        """
        Deques the SQL commands which are not admin commands.

        Returns:
            list: The SQL result with connection information
        """
        if len(self.sql_results) > 0:
            for result in self.sql_results:
                if result[0] != "admin":
                    del self.sql_results[self.sql_results.index(result)]
                    return result
        return ""

    def dequeue_admin_sql(self) -> str:
        """
        Deques the SQL commands from the admin terminal formatted result.

        Returns:
            str: The SQL result formatted with HTML
        """
        if len(self.sql_results) > 0:
            for result in self.sql_results:
                if result[0] == "admin":
                    del self.sql_results[self.sql_results.index(result)]
                    return result[1]
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

    def get_all_sql_commands(self):
        """
        Gets all the sql commands which have been sent from clients to be run by
        the server.
        """
        sql_commands = self.connection_manager.get_all_new_data()
        if sql_commands:
            for command in sql_commands:
                self.enqueue_sql(command)

    def run_sql_commands(self):
        """
        Checks if there are SQL commands then gets the first one and runs it and
        adds the response to the results queue.
        """
        if len(self.sql_commands) > 0:
            sql_command = self.sql_commands.pop(0)
            output = self.database_manager.send_command(sql_command[1])
            self.sql_results.append(
                [sql_command[0], f"{sql_command[1]}\n{self.parse_database_output(output)}"])

    def respond_to_clients(self):
        """
        Sends the responses from the SQL commands to the clients.
        """
        response = self.dequeue_sql()
        while response:
            if response[0] != -1:
                connection_index = self.connection_manager.get_connection_index(response[0])
                self.connection_manager.connections[connection_index].send_data(response[1])
            response = self.dequeue_sql()

    def main_loop(self):
        """
        This function gets called every frame
        """
        self.connection_manager.delete_connections()
        self.get_all_sql_commands()
        self.run_sql_commands()
        self.respond_to_clients()

        self.counter += 1
        if self.counter % EMAIL_CHECK_FREQ == 0:
            self.email_manager.compare_data()
            self.counter = 1

    def change_password(self, new_password:str) -> bool:
        """
        Update the administrator password by hashing the new password, deleting
        the old password and inserting the new password hash.

        Args:
            new_password(str): The ne password to replace the old one with.

        Return:
            bool: whether or not the new password is valid
        """

        if len(new_password) < 5:
            return False

        new_password_hash =  hashlib.md5(new_password.encode("UTF-8")).hexdigest()
        self.database_manager.send_command("DELETE FROM INSTITUTION")
        self.database_manager.send_command(
            f"INSERT INTO INSTITUTION VALUES(\"{new_password_hash}\")")

        return True

    def get_information(self) -> list:
        """
        Get information about the current number of connections, the IP address and port of
        the connections and any queued commands from the connections.

        Returns:
            list: the list of strings to give the admins all information.
        """
        result = [f"There are {len(self.sql_commands)} command(s) to be run.\n"]

        if self.sql_commands:
            result.append("The SQL commands waiting to be run are:\n")
            for sql_command in self.sql_commands:
                result.append(f"{sql_command}\n")

        result.append(
            f"There are {self.connection_manager.get_num_of_connections()} connection(s).\n")

        if self.connection_manager.connections:
            result.append("The addresses of the connections are:\n")
            for connection in self.connection_manager.connections:
                result.append(f"{connection.address}\n")

        return result
