"""
This file holds the class which handles the account management UI.    
"""

import hashlib
import global_vars

from PyQt5 import QtWidgets as qtw

from Ui.AccountWindow import Ui_AccountWindow as account_window

class AccountManager(qtw.QMainWindow):
    """
    This class handles all of the data input and output via the
    account management window.
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.name = ""
        self.email = ""
        self.priority = 0

        self.user_data = global_vars.CONNECTION_MANAGER.send_command(
            "SELECT Email, PasswordHash FROM USERS")

        self.ui = account_window()
        self.ui.setupUi(self)

        self.connect_buttons()
        self.display_widgets()

        self.setFixedSize(400, 300)
        self.setWindowModality(2)
        self.show()

    def connect_buttons(self):
        """
        Connect all of the buttons to their respective functions.
        """
        self.ui.login.clicked.connect(self.login)
        self.ui.logout.clicked.connect(self.logout)

    def display_text(self):
        """
        Display the relevant text in the relevant boxes for the user
        to view their information.
        """
        if global_vars.LOGGED_IN:
            user_display_info = global_vars.CONNECTION_MANAGER.send_command(
                f"SELECT Forename, Surname, Priority, UserID\
                  FROM USERS WHERE Email=\"{global_vars.USER_EMAIL}\"")

            user_display_info=user_display_info[0]
            global_vars.PRIORITY = user_display_info[2]
            global_vars.USER_ID = user_display_info[3]
            self.ui.name.setText(f"{user_display_info[1]}, {user_display_info[0]}")
            self.ui.email.setText(global_vars.USER_EMAIL)
            self.ui.priority.setText(f"Priority: {global_vars.PRIORITY}")
        else:
            self.ui.name.setText("")
            self.ui.email.setText("")
            self.ui.priority.setText("")

    def display_widgets(self):
        """
        Only show the correct widgets whether the user is logged in or
        not logged in.
        """

        self.display_text()

        self.ui.email_in.setVisible(not global_vars.LOGGED_IN)
        self.ui.password.setVisible(not global_vars.LOGGED_IN)
        self.ui.login.setVisible(not global_vars.LOGGED_IN)
        self.ui.logout.setVisible(global_vars.LOGGED_IN)
        self.ui.priority.setVisible(global_vars.LOGGED_IN)
        self.ui.name.setVisible(global_vars.LOGGED_IN)
        self.ui.email.setVisible(global_vars.LOGGED_IN)

    def login(self):
        """
        Log the user in and verify their information.
        """

        password = hashlib.md5(self.ui.password.text().encode("UTF-8")).hexdigest()
        email = self.ui.email_in.text()

        for user in self.user_data:
            if user[0] == email and user[1] == password:
                global_vars.LOGGED_IN = True
                global_vars.USER_EMAIL = email
                self.ui.password.setText("")
                self.display_widgets()

        self.ui.email_in.setText("")


    def logout(self):
        """
        Log the user out if they are already logged in.
        """
        global_vars.LOGGED_IN = False
        self.display_widgets()
