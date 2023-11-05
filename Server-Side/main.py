"""
This is the main file which runs the whole server-side program.

This code runs the main user interface for the server side.

Date: 30/10/2023
Author: Alexander Armitage
"""

import sys
from PyQt5 import QtWidgets as qtw

from user_interface import UserInterface

# This if statement makes sure that the program
# is not run when someone accidentally imports this
# file as a library.
if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    server_side_ui = UserInterface()
    server_side_ui.show()

    app.exec_()

    server_side_ui.end()
    sys.exit()
