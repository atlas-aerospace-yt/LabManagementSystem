"""
Run the client side of the application.

Date: 15/11/2023

Author: Alexander Armitage
"""

import sys
import global_vars
from PyQt5 import QtWidgets as qtw

# This if statement makes sure that the program
# file as a library.
if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    if global_vars.CONNECTION_MANAGER is None:
        error = qtw.QMessageBox.critical(None,
                                        "Startup Error", 
                                        "Could not connect to the server!",
                                        qtw.QMessageBox.Cancel)

    # Only import the UI once a connection is established
    from main_window import MainUI

    client_side_ui = MainUI()
    client_side_ui.show()

    app.exec_()

    global_vars.CONNECTION_MANAGER.end_connection()
