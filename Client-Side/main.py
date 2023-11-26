"""
Run the client side of the application.

Date: 15/11/2023

Author: Alexander Armitage
"""

import sys
from PyQt5 import QtWidgets as qtw

from connection_manager import ConnectionManager
from main_window import MainUI

# This if statement makes sure that the program
# is not run when someone accidentally imports this
# file as a library.
if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    try:
        connection_manager = ConnectionManager()
    except ConnectionRefusedError:
        error = qtw.QMessageBox.critical(None,
                                         "Startup Error", 
                                         "Could not connect to the server!",
                                         qtw.QMessageBox.Cancel)
        sys.exit()

    client_side_ui = MainUI(connection_manager)
    client_side_ui.show()

    app.exec_()

    connection_manager.end_connection()
    sys.exit()
