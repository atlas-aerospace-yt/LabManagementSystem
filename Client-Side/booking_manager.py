"""
This file holds the BookingManager class.
"""

import global_vars

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

import Definitions.gui_definitions as gui

from Ui.BookingWindow import Ui_BookingWindow as booking_window

class BookingManager(qtw.QMainWindow):
    """
    This class handles all interactions with the booking manager.
    """

    def __init__(self, time, date, labs, parent=None):

        if not global_vars.LOGGED_IN or global_vars.PRIORITY == 0:
            return

        super().__init__(parent=parent)

        self.time = time
        self.date = date
        self.labs = labs

        self.stock = []
        self.error = None

        self.ui = booking_window()
        self.ui.setupUi(self)

        # Fill in the QComboBoxes
        stock = global_vars.CONNECTION_MANAGER.send_command(
            "SELECT StockID, Name, Amount FROM STOCK")

        for stock_item in stock:
            self.ui.stock.addItem(stock_item[1])

        for lab in self.labs:
            self.ui.lab.addItem(lab[1])

        self.connect_buttons()

        self.show()

        self.update()
        timer = qtc.QTimer(self)
        timer.setInterval(25)
        timer.timeout.connect(self.update)
        timer.start()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend of the booking manager
        to their respective functions.
        """
        self.ui.add_stock.clicked.connect(self.add_stock)
        self.ui.confirm_booking.clicked.connect(self.commit_booking)

    def update(self):
        """
        Change the text on the browser to show the date, time, and any booked stock
        so the user can see all information.
        """
        html = gui.BOOKING_TITLE_BEGINNING
        html += f"{self.date} at {self.time[1]}-{self.time[2]} in {self.ui.lab.currentText()}"
        html += gui.BOOKING_TITLE_ENDING

        if self.error:
            html += gui.BOOKING_ERROR_BEGINNING
            html += f"Invalid stock amount: \"{self.error}\""
            html += gui.BOOKING_ERROR_ENDING

        for stock in self.stock:
            html += gui.BOOKING_MSG_BEGINNING
            html += f"Booked {stock[1]} of {stock[0]}"
            html += gui.BOOKING_MSG_ENDING

        self.ui.booking_info.setHtml(html)

    def add_stock(self):
        """
        Add a stock item to the booking widget. This verifies the input has entered an integer
        amount that is positive and less than the maximum amount of stock available. This is
        then stored in the self.stock list to be used when the booking is committed.
        """
        already_booked = False

        amount = self.ui.stock_amount.text()
        stock_item = self.ui.stock.currentText()

        max_amount = int(global_vars.CONNECTION_MANAGER.send_command(
            f"SELECT Amount FROM STOCK WHERE Name=\"{stock_item}\"")[0][0])

        if amount.isnumeric() and int(amount) <= max_amount:

            for i, stock in enumerate(self.stock):
                if stock[0] == stock_item:
                    if amount == "0":
                        del self.stock[i]
                    else:
                        self.stock[i][1] = amount
                    already_booked = True
                    continue

            if not already_booked and amount != "0":
                self.stock.append([stock_item, amount])

            self.ui.stock_amount.setText("")
            self.error = None
        else:
            self.error = amount

    def get_booking_id(self):
        """
        Get the first available booking ID that can be used to make a booking.

        Returns:
            int: the first available booking ID
        """
        booking_ids = global_vars.CONNECTION_MANAGER.send_command(
                            "SELECT BookingID FROM BOOKINGS")
        ordered_ids = sorted([int(i[0]) for i in booking_ids])
        used_id = ordered_ids[0]

        if used_id == 0:
            for booking_id in ordered_ids[1:]:
                if used_id+1 != booking_id:
                    print(used_id+1)
                    return used_id+1
                used_id += 1
        else:
            return 0
        return used_id+1

    def get_lab_id(self): # pylint: disable=inconsistent-return-statements
        """
        Find out which lab is selected for the booking and then get the lab ID from
        the database so that the booking can be made.

        The reason for there being no catch all for the return and is condinitional is because
        the condition will always be met as the option is from a drop down and all of the options
        are valid.

        Returns:
            int: the lab ID from the database.
        """
        for lab in self.labs:
            if lab[1] == self.ui.lab.currentText():
                return lab[0]

    def get_stock_items(self):
        """
        Find out which stock items have been booked and place the stock ID and amount
        into a singular list for processing.
        
        Returns:
            list: A 2D list with stock ID and amount.
        """
        stock = []
        for stock_item in self.stock:
            stock.append([global_vars.CONNECTION_MANAGER.send_command(
                f"SELECT * FROM STOCK WHERE Name=\"{stock_item[0]}\"")[0][0], stock_item[1]])
        return stock

    def update_available_stock(self):
        """
        Decrease the amount of available stock by the amount of stock that has been booked.
        """
        for stock in self.stock:
            global_vars.CONNECTION_MANAGER.send_command(
                f"UPDATE STOCK SET Amount=Amount-{stock[1]} WHERE Name=\"{stock[0]}\"")

    def commit_booking(self):
        """
        Commit the booking to the database.
        """
        time_id = self.time[0]
        booking_id = self.get_booking_id()
        lab_id = self.get_lab_id()
        stock = self.get_stock_items()

        self.close()

        # The create booking string needs to be broken into two linesn as it is too long.
        create_booking = f"INSERT INTO BOOKINGS VALUES(\
{booking_id}, {global_vars.USER_ID}, {lab_id}, {time_id}, \"{self.date}\")"

        stock_bookings = []
        for stock_item in stock:
            stock_bookings.append(
                f"INSERT INTO BOOKED_STOCK VALUES ({booking_id}, {stock_item[0]}, {stock_item[1]})")

        # Commit the data to the server-side (THIS CANNOT BE UNDONE)
        global_vars.CONNECTION_MANAGER.send_command(create_booking)
        for stock in stock_bookings:
            global_vars.CONNECTION_MANAGER.send_command(stock)

        self.update_available_stock()
