"""
This file contains the ConnectionManager class for the client
side.

TODO Commenting
TODO Connect with main.py
"""

import socket

PORT = 6556 # a random port
IP_ADDRESS = "127.0.0.1"# local host for testing

class ConnectionManager:
    """
    This class handles the connection between the client side
    and the server side applications.
    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((IP_ADDRESS, PORT))

    def connection_loop(self):
        """
        Loops the connection on a thread.
        """
        while True:
            msg = input("Enter message: ")
            self.client.send(msg.encode("UTF-8")[:1024])

            response = self.client.recv(1024)
            response = response.decode("utf-8")
            
            if response.lower() == "closed":
                break

            print(f"Received: {response}")
        
        self.client.close()
        print("Connection to server closed")

    def send_data(self, data):
        """
        This function sends data to the client side such as SQL outputs.
        
        Args:
            data(str): the data that is to be sent to the client side
        """
        data = data.encode("utf-8")
        self.socket.send(data)


# Check if this file is being run this loop is inspired by:
# https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
if __name__ == "__main__":

    my_connection = ConnectionManager()
    my_connection.connection_loop()
