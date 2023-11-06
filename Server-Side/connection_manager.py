"""
This file contains the ConnectionManager class

The code is inspired by:
https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python

TODO Commenting
TODO Connect with main.py
"""

import time
import socket
import threading

PORT = 6556 # a random port
IP_ADDRESS = "127.0.0.1" # local host for testing

class Connection:
    """
    The connection class creates a connection object for
    ease of manaing connections.
    """

    def __init__(self, client_socket, client_address):
        self.socket = client_socket
        self.address = client_address
        self.disconnected = False
        self.running = True
        self.data = []

        self.connection = threading.Thread(target=self.connection_loop)
        self.connection.start()

    def connection_loop(self):
        """
        Loops the connection on a thread.
        """
        while self.running:
            try:
                request = self.socket.recv(1024)
                request = request.decode("utf-8")
            except (ConnectionResetError, ConnectionAbortedError):
                break

            if request.lower() == "close":
                self.socket.send("closed".encode("utf-8"))
                break

            print(f"Received: {request}")
            response = "accepted".encode("utf-8")
            self.socket.send(response)
            time.sleep(2)

        self.disconnected = True

    def send_data(self, data):
        """
        This function sends data to the client side such as SQL outputs.
        
        Args:
            data(str): the data that is to be sent to the client side
        """
        data = data.encode("utf-8")
        self.socket.send(data)

    def disconnect(self):
        """
        Disconnects the user from the server.
        """
        self.socket.close()


class ConnectionManager:
    """
    The connection manager class deals with the connections
    between the client side and the server side
    """

    def __init__(self):
        self.new_data = False
        self.running = True
        self.connections = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((IP_ADDRESS, PORT))

        self.get_connections = threading.Thread(target=self.get_connection)
        self.get_connections.start()

    def get_connection(self):
        """
        Loops waiting for connections to add them to the connections list.
        """
        while self.running:
            print(f"Server listening... Number of connections: {len(self.connections)}")
            self.server.listen(0)

            client_socket, client_address = self.server.accept()
            print(f"Added a new connection to: {client_address[0]}:{client_address[1]}")
            self.connections.append(Connection(client_socket, client_address))

    def get_num_of_connection(self) -> int:
        """
        Gets the number of connections to the server.

        Returns:
            int: the number of connected users.
        """
        return len(self.connections)

    def get_all_new_data(self) -> list:
        """
        Gets the commands which have been sent from the connections

        Returns:
            list: the data to be processed.
        """
        commands = []
        for connection in self.connections:
            for command in connection.data:
                commands.append(command)

    def end_connections(self):
        """
        Deletes all connections to the clients.
        """
        self.running = False

        for i, connection in enumerate(self.connections):
            connection.running = False
            connection.disconnect()

            del self.connections[i]
        
        # Break out of the loop
        fake_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fake_connection.connect((IP_ADDRESS, PORT))
        fake_connection.send("close".encode("UTF-8"))
        fake_connection.close()


# Check if this file is being run
if __name__ == "__main__":
    my_server = ConnectionManager()
    while True:
        for item in my_server.connections:
            if item.disconnected is True:
                del my_server.connections[my_server.connections.index(item)]
                print(f"Removed: {item.address[0]}:{item.address[1]}")
