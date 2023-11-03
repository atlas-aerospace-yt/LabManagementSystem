"""
This file contains the ConnectionManager class

The code is inspired by:
https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
"""

import socket

PORT = 6556
IP_ADDRESS = "127.0.0.1" # local host for testing

class Connection:
    """
    The connection class creates a connection object for
    ease of manaing connections.
    """

    def __init__(self, client_socket, client_address):
        self.socket = client_socket
        self.address = client_address
        self.data = []


class ConnectionManager:
    """
    The connection manager class deals with the connections
    between the client side and the server side
    """

    def __init__(self):
        self.new_data = False
        self.connections = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((IP_ADDRESS, PORT))

        print("Server listening...")
        self.server.listen(0)

    def get_new_data(self) -> list:
        """
        Returns the commands which have been sent from the connections

        Returns:
            list: the data to be processed.
        """


