"""
This file contains the ServerManager class.
"""
import threading

from database_manager import DatabaseManager

GREETING = "Welcome to the admin terminal!\n"

INVALID_INPUT = "Invalid input!\n"

MENU = """The options for the admin terminal are:\n
    \"exit\" - ends the server side program.
    \"disconnect-\"(all or ip) - disconects a specific user or all.
    \"get_info\" - to get information about the activity.
    \"SQL-\"(command) - run an SQL command on the servers\n"""

COMMAND_LIST = ["disconnect",
                "get_info"]


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
        self.terminal_thread = threading.Thread(target=self.threaded_admin_input)
        self.admin_commands = []
        self.sql_commands = []
        self.running = True

        # TODO add the other managers
        #self.connection_manager = ConnectionManager()
        self.database_manager = DatabaseManager()

    def start_admin_terminal(self):
        """
        This function triggers the admin terminal.
        """
        self.terminal_thread.start()

    def threaded_admin_input(self):
        """
        This function threads the administrator input.
        """
        print(GREETING)
        print(MENU)

        command = ""
        invalid = False

        while command.lower() != "exit":
            if invalid:
                print(INVALID_INPUT)
                print(MENU)
            invalid = True
            command = input(">>> ")
            if command[:3].lower() == "sql":
                command = command[4:]
                self.sql_commands.append(command)
                invalid = False
            else:
                for cmd in COMMAND_LIST:
                    if command.lower()[:len(cmd)] == cmd:
                        print("Your command: " + command[len(cmd)+1:])
                        invalid = False
                        break

        self.running = False