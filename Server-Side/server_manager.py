"""
This file contains the ServerManager class.
"""

from database_manager import DatabaseManager
from connection_manager import ConnectionManager

GREETING = "Welcome to the admin terminal!\n"

INVALID_INPUT = "Invalid input!\n"

COMMAND_LIST = {"disconnect":"(all or ip) - disconects a specific user or all.",
                "info":"to get information about the activity."}

MENU = """The options for the admin terminal are:\n
    \"exit\" - ends the server side program.
    \"SQL\"(command) - run an SQL command on the servers\n"""

for menu_item in list(COMMAND_LIST.keys()):
    MENU += f"    \"{menu_item}\" - {COMMAND_LIST[menu_item]}\n"

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
        self.admin_commands = []
        self.sql_commands = []

        self.connection_manager = ConnectionManager()
        self.database_manager = DatabaseManager()

    #def threaded_admin_input(self):
#
 #       This function threads the administrator input as the database cannot
  #      be accessed by another thread so the main thread needs to be the
   #     database.
#
 #       print(GREETING)
  #      print(MENU)
#
 #       command = ""
  #      invalid = False
#
 #       while command.lower() != "exit":
#
 #           # Wait for the last command to run
  #          while "admin" in self.sql_commands:
   #             pass
    #        # TODO complete the admin commands
     #       #while len(self.admin_commands) > 0:
      #      #    pass
#
 #           # Help the user if the command was invalid
  #          if invalid:
   #             print(INVALID_INPUT)
    #            print(MENU)
     #       invalid = True
      #       command = input(">>> ")

            # Process the commands
      #      if command[:3].lower() == "sql":
       #         command = command[4:]
        #        self.sql_commands["admin"] = command
         #       invalid = False
          #  elif command == "":
           #     invalid = False
            #else:
             #   for cmd in COMMAND_LIST:
              #      if command.lower()[:len(cmd)] == cmd:
               #         self.admin_commands.append(command[len(cmd)+1:])
                #        invalid = False
                 #       break


    def enque_sql(self, command:str):
        """
        Enque an SQL command which is to be run.
        
        Args:
            command(str): the SQL command
        """
        self.sql_commands.append(["admin", command])

    def parse_database_output(self, output:list):
        """
        This function processes the output which is returned from the database
        manager so that it is easy to read on screen for the admins.

        Args:
            ouptut(list): the string that has been output by the database manager
        """
        for item in output:
            if item is not None:
                print(item)

    def main_loop(self):
        """
        This function gets called every frame
        """

        # remove all disconnected users
        for item in self.connection_manager.connections:
            if item.disconnected is True:
                del self.connection_manager.connections[
                    self.connection_manager.connections.index(item)]
                print(f"Removed: {item.address[0]}:{item.address[1]}")
                print(">>> ", end="")

        # Check if there is an SQL command to run
        if len(self.sql_commands) > 0:
            sql_command = self.sql_commands.pop(0)
            output = self.database_manager.send_command(sql_command[1])

            # Check if the command is an admin command
            if sql_command[0] == "admin":
                self.parse_database_output(output)
