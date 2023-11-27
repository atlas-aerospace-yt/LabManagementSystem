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

    def __init__(self, logged_in, parent=None):
        super().__init__(parent=parent)

        self.is_logged_in = logged_in

        self.name = ""
        self.email = ""
        self.priority = 0

        self.ui = account_window()
        self.ui.setupUi(self)

        self.connect_buttons()
        self.display_widgets()

        self.show()

    def connect_buttons(self):
        """
        Connect all of the buttons to their respective functions.
        """
        self.ui.login.clicked.connect(self.login)
        self.ui.logout.clicked.connect(self.logout)

    def display_widgets(self):
        """
        Only show the correct widgets whether the user is logged in or
        not logged in.
        """
        if self.is_logged_in:
            self.ui.email_in.setVisible(False)
            self.ui.name_in.setVisible(False)
            self.ui.login.setVisible(False)
            self.ui.logout.setVisible(True)
            self.ui.priority.setVisible(True)
            self.ui.name.setVisible(True)
            self.ui.email.setVisible(True)
        else:
            self.ui.email_in.setVisible(True)
            self.ui.name_in.setVisible(True)
            self.ui.login.setVisible(True)
            self.ui.logout.setVisible(False)
            self.ui.priority.setVisible(False)
            self.ui.name.setVisible(False)
            self.ui.email.setVisible(False)

    def login(self):
        """
        Log the user in and verify their information.
        """
        print("Logging in...")
        self.is_logged_in = True
        self.display_widgets()

    def logout(self):
        """
        Log the user out if they are already logged in.
        """
        print("Logging out...")
