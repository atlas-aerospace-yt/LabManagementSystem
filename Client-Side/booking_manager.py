"""
This file holds the BookingManager class.

TODO -> all functions that say "pass".
"""

from PyQt5 import QtWidgets as qtw

from Ui.BookingWindow import Ui_BookingWindow as booking_window

class BookingManager(qtw.QMainWindow):
    """
    This class handles all interactions with the booking manager.
    """

    def __init__(self, connection_manager, time, date, labs, parent=None):
        super().__init__(parent=parent)
        self.connection_manager = connection_manager
        print(time)
        print(date)
        print(labs)
        print(self.connection_manager.send_command("SELECT StockID, Name, Amount FROM STOCK"))
        self.ui = booking_window()
        self.ui.setupUi(self)

        self.connect_buttons()

        self.show()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend of the booking manager
        to their respective functions.
        """
        self.ui.add_stock.clicked.connect(self.add_stock)
        self.ui.confirm_booking.clicked.connect(self.commit_booking)

    def show_stock(self):
        """
        Show the available stock in the drop down widget.
        """
        pass

    def show_labs(self):
        """
        Show the avaliable labs in the drop down widget.
        """
        pass

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
