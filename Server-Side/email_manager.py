"""
This file sends out email communications when things
such as stock or bookings changes.

This code uses some functions which were found in:
https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/

TODO everything
"""


import smtplib

class EmailManager:
    """
    Handle email communications.
    """

    def __init__(self, database_manager):
        self.email = smtplib.SMTP('smtp.gmail.com', 587)
        self.email.starttls()
        self.email.login("enter_email","enter_pass")

        self.database_manager = database_manager

        # Get the baseline data
        self.previous_data = [
            self.database_manager.send_command("SELECT * FROM STOCK"),
            self.database_manager.send_command("SELECT * FROM BOOKINGS"),
            self.database_manager.send_command("SELECT * FROM USERS")
        ]

        self.data = self.previous_data

    def send_message(self):
        """
        Send the update message to the intended recipients.
        """
        pass

    def compare_data(self):
        """
        Compare the data in the database now compared to how it was previously
        and check if any emails need to be sent out.
        """
        pass

    def close_email(self):
        """
        Close the tls connection when the app closes.
        """
        self.email.close()