"""
This file holds the class which handles the account management UI.    
"""

from PyQt5 import QtWidgets as qtw

from Ui.AccountWindow import Ui_AccountWindow as account_window

class AccountManager(qtw.QMainWindow):
    """
    This class handles all of the data input and output via the
    account management window.
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.ui = account_window()
        self.ui.setupUi(self)

        self.ui.email_in.setVisible(False)
        self.ui.login.setVisible(False)
        self.ui.name_in.setVisible(False)

        self.show()

    def connect_buttons(self):
        """
        Connect all of the buttons to their respective functions.
        """
        self.ui.login.clicked.connect(self.login)
        self.ui.logout.clicked.connect(self.logout)

    def login(self):
        """
        Log the user in and verify their information.
        """
        print("Logging in...")

    def logout(self):
        """
        Log the user out if they are already logged in.
        """
        print("Logging out...")
