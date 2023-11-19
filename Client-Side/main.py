"""
Run the client side of the application.

Date: 15/11/2023

Author: Alexander Armitage
"""

import sys
from PyQt5 import QtWidgets as qtw

from main_window import MainUI

# This if statement makes sure that the program
# is not run when someone accidentally imports this
# file as a library.
if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    server_side_ui = MainUI()
    server_side_ui.show()

    app.exec_()
    sys.exit()
