"""
This file contains the ConnectionManager class

The code is inspired by:
https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
"""

import socket
import threading

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

        self.get_connections = threading.Thread(target=self.threaded_get_connection())
        self.get_connections.start()

    def threaded_get_connection(self):
        """
        Loops waiting for connections to add them to the connections list.
        """
        while True:
            print(f"Server listening... Number of connections: {len(self.connections)}")
            self.server.listen(0)

            client_socket, client_address = self.server.accept()
            self.connections.append(Connection(client_socket, client_address))
            print(f"Added a new connection to: {client_address[0]}:{client_address[1]}")

    def get_new_data(self) -> list:
        """
        Gets the commands which have been sent from the connections

        Returns:
            list: the data to be processed.
        """
        pass

# Check if this file is being run
if __name__ == "__main__":
    my_connection = ConnectionManager()

