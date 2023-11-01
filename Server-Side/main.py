"""
This is the main file which runs the whole server-side program.

This code imports all libraries (custom and PIP) and runs the
main loop.

Date: 30/10/2023
Author: Alexander Armitage
"""

# TODO get all libraries
from server_manager import ServerManager

# This if statement makes sure that the program
# is not run when someone accidentally imports this
# file as a library.
if __name__ == "__main__":

    # TODO main loop
    my_server = ServerManager()
    my_server.start_admin_terminal()
    while my_server.running:
        pass

    # TODO At the end of the main loop
    my_server.database_manager.end_connection()
