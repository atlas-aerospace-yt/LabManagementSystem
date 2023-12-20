"""
This file contains the UserInterface class.    
"""

import hashlib

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

import Definitions.gui_definitions as gui

from server_manager import ServerManager
from Ui.server_side import Ui_MainWindow as terminal

class UserInterface(qtw.QMainWindow):
    """
    Launches the server side terminal which is a GUI.

    Args:
        qtw (QtWidgets): the main window functions
    """

    def __init__(self):
        super().__init__()

        self.ui = terminal()
        self.server = ServerManager()

        self.message_attributes = [gui.MSG_LOGIN]
        self.prev_num_of_messages = 0

        self.logged_in = False

        self.ui.setupUi(self)
        self.connect_buttons()

        timer = qtc.QTimer(self)
        timer.setInterval(100)
        timer.timeout.connect(self.loop)
        timer.start()

    def connect_buttons(self):
        """
        Connects the enter key to the loop 
        """
        self.ui.command.returnPressed.connect(self.add_command)

    def loop(self):
        """
        Calls the main loop every 100ms.
        TODO -> Tidy up this function
        """
        # Loop the backend main loop
        self.server.main_loop()

        # Update the number of connections displayed on the screen
        connections = self.server.connection_manager.get_num_of_connections()
        self.ui.num_of_connections.setText(f"Connections: {connections}")

        # Add new results to the messages
        results = self.server.dequeue_admin_sql()

        for result in reversed(results.split("\n")):
            if result:
                self.message_attributes.insert(1, result)

        if len(self.message_attributes) != self.prev_num_of_messages:
            self.update_html()
            self.prev_num_of_messages = len(self.message_attributes)

        # Syntax from:
        # https://stackoverflow.com/questions/23634843/password-form-in-pyqt
        if not self.logged_in:
            self.ui.command.setEchoMode(qtw.QLineEdit.Password)
        else:
            self.ui.command.setEchoMode(qtw.QLineEdit.Normal)

    def update_html(self):
        """
        Update the html being displayed.
        """
        html = self.message_attributes[0]
        for message in self.message_attributes[1:]:
            html += gui.MSG_BEGINNING + message + gui.MSG_ENDING
        self.ui.terminal.setHtml(html)

    def add_command(self):
        """
        Queues and parses the commands into the different types.
        TODO -> Tidy up this function
        """
        command = self.ui.command.text()
        self.ui.command.setText("")

        if len(command) > 10:
            valid_string = command[10:].count("-") == 2 and command[10:].count(".") == 3
            valid_string = valid_string and command.split("-")[2].isnumeric()

        if not self.logged_in:
            self.verify_login(command)
            return

        elif command.lower() == gui.EXIT:
            self.close()

        elif command[:3].lower() == gui.SQL:
            self.server.enqueue_sql(["admin", command[4:]])

        elif command[:5].lower() == gui.RESET:
            if self.server.change_password(command[6:]):
                self.message_attributes.insert(1, gui.RESET_PASSWORD_SUCC)
            else:
                self.message_attributes.insert(1, gui.RESET_PASSWORD_FAIL)

        elif command[:6].lower() == gui.LOGOUT:
            self.logged_in = False
            self.message_attributes = [gui.MSG_LOGIN]

        elif command[:4].lower() == gui.INFO:
            msgs = self.server.get_information()
            for i, msg in enumerate(msgs):
                self.message_attributes.insert(i+1, msg)

        elif command[:10].lower() == gui.DISCONNECT and command[-2:] == "-a":
            self.server.connection_manager.end_connections()
            self.server.connection_manager.running = True
            self.message_attributes.insert(1, gui.DISCONNECT_ALL)

        elif command[:10].lower() == gui.DISCONNECT and valid_string:
            target = (command.split("-")[1], int(command.split("-")[2]))
            disconnected = self.server.connection_manager.end_connection(target)
            if disconnected:
                self.message_attributes.insert(1, gui.DISCONNECT_SPECIFIC + str(target))
            else:
                self.message_attributes.insert(1, gui.DISCONNECT_SPECIFIC_FAIL)

        elif command[:5].lower() == gui.CLEAR:
            self.message_attributes = [self.message_attributes[0], self.message_attributes[-1]]

        else:
            self.message_attributes.insert(1, f"Invalid input: \"{command}\"")


    def verify_login(self, password:str):
        """
        Checks the login against what is stored in the INSTITUTION database using
        an md5 hash.

        Args:
            password(str): the password that the user has entered.
        """
        input_password = hashlib.md5(password.encode("UTF-8")).hexdigest()
        actual_password = self.server.database_manager.send_command(gui.GET_PWD_HASH)[0][0]

        if input_password == actual_password:
            self.message_attributes = [gui.MSG_INSTRUCTIONS, "Logged in!"]
            self.prev_num_of_messages = -1
            self.logged_in = True
        else:
            self.message_attributes.append(gui.INVALID_PASSWORD)

    def end(self):
        """
        Ends all connections to the database and to the client devices.
        """
        self.server.database_manager.end_connection()
        self.server.connection_manager.end_server()
        self.server.connection_manager.end_connections()
