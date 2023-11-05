"""
This file contains the UserInterface class.    
"""

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

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
        self.ui.setupUi(self)
        self.server = ServerManager()

        self.connect_buttons()

        timer = qtc.QTimer(self)
        timer.setInterval(25)
        timer.timeout.connect(self.loop)
        timer.start()

    def connect_buttons(self):
        """
        Connects the enter key to the loop 
        """

        self.ui.command.returnPressed.connect(self.add_command)

    def loop(self):
        """
        Calls the main loop every 25ms.
        """
        self.server.main_loop()
        connections = self.server.connection_manager.get_num_of_connection()
        self.ui.num_of_connections.setText(f"Connections: {connections}")

    def add_command(self):
        """
        Queues and parses the commands into the different types.
        """
        command = self.ui.command.text()

        if command[:3].lower() == "sql":
            self.server.enque_sql(command[4:])

        self.ui.command.setText("")

    def end(self):
        """
        Ends all connections to the database and to the client devices
        TODO
        """
        self.server.database_manager.end_connection()
        self.server.connection_manager.end_connections()
