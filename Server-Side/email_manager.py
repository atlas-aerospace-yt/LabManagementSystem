"""
This file sends out email communications when things
such as stock or bookings changes.

This code uses some functions which were found in:
https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
"""

import smtplib
import copy

from email.message import EmailMessage

# This email neeeds to be changed to the email that receives
# institution wide notifications.
INSTITUTION_EMAIL = "INSTITUTION_EMAIL"

# This is the email which sends out the notification to all of
# the recipients.
SENDER_EMAIL = "SENDER_EMAIL"
SENDER_PASS = "APP_PASSWORD"

class EmailManager:
    """
    Handle email communications when changes are made to the database. Then
    check which changes were made and send out the correct notification.
    """

    def __init__(self, database_manager):
        self.email = smtplib.SMTP('smtp.gmail.com', 587)
        self.email.starttls()
        #self.email.login(SENDER_EMAIL, SENDER_PASS)

        self.database_manager = database_manager

        # Get the baseline data
        self.previous_data = [
            self.database_manager.send_command("SELECT * FROM STOCK"),
            self.database_manager.send_command("SELECT * FROM BOOKINGS")
        ]

        self.data = self.previous_data

    def send_new_stock_email(self, new_stock):
        """
        Send an email to the institution which informs them of the new stock being added.

        Args:
            new_stock(list): this is the new stock item to update the institution about.
        """
        name = new_stock[1]
        amount = new_stock[2]
        price = new_stock[3]
        website = new_stock[4]
        supplier_name = self.database_manager.send_command(
            f"SELECT * FROM SUPPLIER WHERE SupplierID={new_stock[5]}")[0][1]

        email = "Stock update!\n\nThe new stock item is as follows:\n"
        email += f"Name: {name}\n"
        email += f"Amount: {amount}\n"
        email += f"Price: £{price/100}\n"
        email += f"Website: {website}\n"
        email += f"Supplier: {supplier_name}\n"
        email += "\nFrom:\nLab management"

        msg  = EmailMessage()
        msg.set_content(email)
        msg["Subject"] = "Added stock"
        msg["From"] = SENDER_EMAIL
        msg["To"] = INSTITUTION_EMAIL

        print(email)
        #self.email.send_message(msg)

    def send_delete_stock_email(self, old_stock):
        """
        Send an email to the institution which informs them of a stock item being deleted.
        """
        name = old_stock[1]
        amount = old_stock[2]
        price = old_stock[3]
        website = old_stock[4]
        supplier_name = self.database_manager.send_command(
            f"SELECT * FROM SUPPLIER WHERE SupplierID={old_stock[5]}")[0][1]

        email = "Stock update!\n\nThe stock item that was deleted is as follows:\n"
        email += f"Name: {name}\n"
        email += f"Amount: {amount}\n"
        email += f"Price: £{price/100}\n"
        email += f"Website: {website}\n"
        email += f"Supplier: {supplier_name}\n"
        email += "\nFrom:\nLab management"

        msg  = EmailMessage()
        msg.set_content(email)
        msg["Subject"] = "Deleted stock"
        msg["From"] = SENDER_EMAIL
        msg["To"] = INSTITUTION_EMAIL

        print(email)
        #self.email.send_message(msg)

    def send_modified_stock_email(self, new_stock, old_stock):
        """
        Send an email to the institution which informs them of a stock amount changing.
        """
        name = old_stock[1]
        old_amount = old_stock[2]
        new_amount = new_stock[2]
        price = old_stock[3]

        email = "Stock update!\n\n"
        email += f"The stock item {name}'s amount changed from {old_amount} to {new_amount}.\n"
        email += f"The price of this item is recorded as £{price/100}.\n"
        email += "\nFrom:\nLab management"

        msg  = EmailMessage()
        msg.set_content(email)
        msg["Subject"] = "Stock item has changed"
        msg["From"] = SENDER_EMAIL
        msg["To"] = INSTITUTION_EMAIL

        print(email)
        #self.email.send_message(msg)

    def check_for_stock_notification(self, data:list, prev_data:list):
        """
        Check what types of changes have happened to the stock item.
        """
        # Create a deep copy so as to not edit the class variables
        data = copy.deepcopy(data)
        prev_data = copy.deepcopy(prev_data)

        # Make the lists the same length putting None in the filling spaces
        i = 0
        while len(data) != len(prev_data):
            if i >= len(data):
                data.append(None)
            elif i >= len(prev_data):
                prev_data.append(None)
            elif data[i][0] != prev_data[i][0]:
                if data[i][0] > prev_data[i][0]:
                    data.insert(i, None)
                else:
                    prev_data.insert(i, None)
            i += 1

        # Check which changes have occured
        for new_data, old_data in zip(data, prev_data):
            if new_data != old_data and old_data is None:
                self.send_new_stock_email(new_data)
            elif new_data != old_data and new_data is None:
                self.send_delete_stock_email(old_data)
            elif new_data != old_data and new_data[1] != old_data[1]:
                self.send_new_stock_email(new_data)
                self.send_delete_stock_email(old_data)
            elif new_data != old_data:
                self.send_modified_stock_email(new_data, old_data)

    def send_bookings_notification(self, data:list, prev_data:list):
        """
        Send a booking notification update to the intended recipients.
        """
        new_data = [booking for booking in data if booking not in prev_data]

        for booking in new_data:

            booked_time = self.database_manager.send_command(
                f"SELECT StartTime, EndTime FROM TIMETABLE WHERE TimeID={booking[3]}")[0]
            lab = self.database_manager.send_command(
                f"SELECT Name FROM LABS WHERE LabID={booking[2]}")[0][0]
            recv_email = self.database_manager.send_command(
                f"SELECT Email FROM USERS WHERE UserID={booking[1]}")[0][0]

            email = "New booking notification!\n\n"
            email += f"You have a new booking on {booking[4]}"
            email += f" at {booked_time[0]}-{booked_time[1]}.\n"
            email += f"The booking is in the lab \"{lab}\".\n"
            email += "\nFrom:\nLab management"

            msg  = EmailMessage()
            msg.set_content(email)
            msg["Subject"] = "New booking"
            msg["From"] = SENDER_EMAIL
            msg["To"] = INSTITUTION_EMAIL + ", " + recv_email

            print(email)
            #self.email.send_message(msg)

    def compare_data(self):
        """
        Compare the data in the database now compared to how it was previously
        and check if any emails need to be sent out.
        """
        self.data = [
            self.database_manager.send_command("SELECT * FROM STOCK"),
            self.database_manager.send_command("SELECT * FROM BOOKINGS")
        ]

        # If there is no change, don't do anything.
        if self.data == self.previous_data:
            return

        # Send the relevant emails.
        if self.data[0] != self.previous_data[0]:
            self.check_for_stock_notification(self.data[0], self.previous_data[0])
        if self.data[1] != self.previous_data[1]:
            self.send_bookings_notification(self.data[1], self.previous_data[1])

        self.previous_data = self.data

    def close_email(self):
        """
        Close the tls connection when the app closes.
        """
        self.email.close()
