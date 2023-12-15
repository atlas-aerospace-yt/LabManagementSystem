"""
This file contains the ConnectionManager class for the client
side.

TODO Commenting
TODO Connect with main.py
"""

import socket
import threading

PORT = 6556 # a random port
IP_ADDRESS = "127.0.0.1"# local host for testing

class ConnectionManager:
    """
    This class handles the connection between the client side
    and the server side applications.
    """

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((IP_ADDRESS, PORT))

        self.data = None
        self.running = True

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
                request = b""

                while self.running:
                    data = self.server.recv(1024)
                    request += data
                    if "\r\n" in request.decode("utf-8"):
                        break
                request = request.decode("utf-8").split("\r\n")[0]

            except (ConnectionResetError, ConnectionAbortedError):
                break
            if request.lower() == "closed":
                break
            self.data = request

        self.server.close()
        self.running = False
        print("Connection to server closed")

    def parse_result(self, data:str):
        """
        Parse the data from the server side so it is somewhat usable.

        Args:
            data(str): the result from the server side
        """
        if "syntax error" in data:
            return None
        if "No data returned!" in data:
            return []

        output = []
        data_list = data.split("\n")[1:-1]

        for i, data_record in enumerate(data_list):
            data_record = data_record[1:-1]
            output.append([])
            for data_point in data_record.split(", "):
                if data_point.endswith(","):
                    output[i].append(data_point[0:-1])
                elif data_point.startswith("'") and data_point.endswith("'"):
                    output[i].append(data_point.replace("'",""))
                elif data_point.isnumeric():
                    output[i].append(int(data_point))
                else:
                    output[i].append(float(data_point))
        return output

    def send_command(self, data:str):
        """
        This function sends data to the client side such as SQL outputs.
        
        Args:
            data(str): the data that is to be sent to the client side
        """
        data = data.replace("\n"," ").encode("utf-8")
        self.server.send(data)

        # Wait for there to be a response from the server
        while not self.data:
            pass

        result = self.data
        self.data = None
        return self.parse_result(result)

    def end_connection(self):
        """
        Close the connection between the server side and client side.
        """
        self.running = False
        self.server.send("close\r\n".encode("UTF-8"))
        # Wait for the server to respond.
        while self.running:
            pass


def test_function():
    """
    Test the connection manager.
    """
    my_connection = ConnectionManager()

    usr_input = ""
    while usr_input != "exit":
        usr_input = input("Enter SQL command: ")
        print(my_connection.send_command(usr_input))

# Check if this file is being run this loop is inspired by:
# https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
if __name__ == "__main__":
    test_function()
