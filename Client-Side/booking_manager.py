"""
This file holds the BookingManager class.

TODO -> all functions that say "pass".
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

        self.ui = booking_window()
        self.ui.setupUi(self)

        # Fill in the QComboBoxes
        stock = global_vars.CONNECTION_MANAGER.send_command(
            "SELECT StockID, Name, Amount FROM STOCK")

        for stock_item in stock:
            self.ui.stock.addItem(stock_item[1])

        for lab in labs:
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
        html += f"{self.date} at {self.time[1]}-{self.time[2]}"
        html += gui.BOOKING_MSG_ENDING

        self.ui.booking_info.setHtml(html)

    def add_stock(self):
        """
        Add a stock item to the booking widget.
        """
        print("Adding stock...")

    def commit_booking(self):
        """
        Commit the booking to the database.
        """
        print("Committing booking...")
