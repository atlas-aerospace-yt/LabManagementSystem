"""
This file contains the ConnectionManager class for the client
side.
"""

import socket

PORT = 6556
IP_ADDRESS = "127.0.0.1"

class ConnectionManager:
    """
    This class handles the connection between the client side
    and the server side applications.
    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((IP_ADDRESS, PORT))

# Check if this file is being run
if __name__ == "__main__":
    my_connection = ConnectionManager()
    while True:
        pass