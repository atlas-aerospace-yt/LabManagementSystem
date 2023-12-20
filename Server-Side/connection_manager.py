"""
This file contains the ConnectionManager class

The code is inspired by:
https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
"""

import time
import socket
import threading

# local host for testing
PORT = 6556
IP_ADDRESS = "127.0.0.1"

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
            # This prevents connection problems to one client from crashing
            # the whole server side program.
            try:
                request = self.socket.recv(1024)
                request = request.decode("utf-8")
            except (ConnectionResetError, ConnectionAbortedError):
                break

            if request.lower() == "close":
                self.socket.send("close".encode("utf-8"))
                break

            self.data.append([self.address, request])
            time.sleep(2)

        self.disconnected = True

    def send_data(self, data):
        """
        This function sends data to the client side such as SQL outputs.
        
        Args:
            data(str): the data that is to be sent to the client side
        """
        data = (data + "\r\n").encode("utf-8")
        self.socket.send(data)

    def disconnect(self):
        """
        Disconnects the user from the server.
        """
        self.socket.send("close".encode("utf-8"))
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
            self.server.listen(0)
            client_socket, client_address = self.server.accept()
            self.connections.append(Connection(client_socket, client_address))

    def get_num_of_connections(self) -> int:
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
                del connection.data[connection.data.index(command)]

        return commands

    def get_connection_index(self, address:tuple) -> int:
        """
        Gets the index of a specific client that is connected.

        Args:
            address (tuple): the ip address and port

        Returns:
            int: the index of the connection in self.connections (-1 if doesnt exist)
        """
        for connection in self.connections:
            if connection.address == address:
                return self.connections.index(connection)
        return -1

    def delete_connections(self):
        """
        Removes all of the clients who have disconnected from the list.
        """
        deleted_connections = []
        for i, connection in enumerate(self.connections):
            if connection.disconnected is True:
                deleted_connections.append(i)
        # Delete the connections from the list after all are disconnected.
        for indx in deleted_connections:
            del self.connections[indx]

    def end_connection(self, target:tuple) -> bool:
        """
        End a specific connection given an IP address and port.

        Args:
            target(tuple): the information of the target.

        Returns:
            bool: whether or not the connection did exist
        """
        for i, connection in enumerate(self.connections):
            if target == connection.address:
                connection.disconnect()
                del self.connections[i]
                return True
        return False

    def end_connections(self):
        """
        Deletes all connections to the clients.
        """
        for i, connection in enumerate(self.connections):
            connection.running = False
            connection.disconnect()
        for i, _ in enumerate(self.connections):
            del self.connections[i]

    def end_server(self):
        """
        Stops the server from listening for more clients.
        """
        self.running = False
        fake_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fake_connection.connect((IP_ADDRESS, PORT))
        fake_connection.send("close".encode("UTF-8"))
        fake_connection.close()
