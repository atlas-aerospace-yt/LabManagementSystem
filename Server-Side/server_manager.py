"""
This file contains the ServerManager class.
"""
import threading
import time

from database_manager import DatabaseManager

GREETING = "Welcome to the admin terminal!\n"

INVALID_INPUT = "Invalid input!\n"

COMMAND_LIST = {"disconnect":"(all or ip) - disconects a specific user or all.",
                "info":"to get information about the activity."}

MENU = """The options for the admin terminal are:\n
    \"exit\" - ends the server side program.
    \"SQL\"(command) - run an SQL command on the servers\n"""

for item in list(COMMAND_LIST.keys()):
    MENU += f"    \"{item}\" - {COMMAND_LIST[item]}\n"

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
        self.sql_commands = {}
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
        This function threads the administrator input as the database cannot
        be accessed by another thread so the main thread needs to be the
        database.
        """
        print(GREETING)
        print(MENU)

        command = ""
        invalid = False

        while command.lower() != "exit":

            # Wait for the last command to run
            while "admin" in list(self.sql_commands.keys()):
                pass
            # TODO complete the admin commands
            #while len(self.admin_commands) > 0:
            #    pass

            # Help the user if the command was invalid
            if invalid:
                print(INVALID_INPUT)
                print(MENU)
            invalid = True
            command = input(">>> ")

            # Process the commands
            if command[:3].lower() == "sql":
                command = command[4:]
                self.sql_commands["admin"] = (command)
                invalid = False
            elif command == "":
                invalid = False
            else:
                for cmd in COMMAND_LIST:
                    if command.lower()[:len(cmd)] == cmd:
                        self.admin_commands.append(command[len(cmd)+1:])
                        invalid = False
                        break

        self.running = False

    def parse_database_output(self, output):
        """
        This function processes the output which is returned from the database
        manager so that it is easy to read on screen for the admins.

        Args:
            ouptut(str): the string that has been output by the database manager
        """
        for item in output:
            if item is not None:
                print(item)

    def main_loop(self):
        """
        This is the continuous loop which manages the server side of
        the application. It processes commands (admin and sql) with
        the use of a queue.
        """

        while self.running:

            # Check if there is a command to run
            sql_keys = list(self.sql_commands.keys())
            if len(sql_keys) > 0:
                sql_command = self.sql_commands[sql_keys[0]]
                output = self.database_manager.send_command(sql_command)

                if sql_keys[0] == "admin":
                    self.parse_database_output(output)

                del self.sql_commands[sql_keys[0]]