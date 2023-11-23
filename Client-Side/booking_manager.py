"""
This file holds the BookingManager class.
"""

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from Ui.BookingWindow import Ui_BookingWindow as booking_window

class BookingManager(qtw.QMainWindow):
    """
    This class handles all interactions with the booking manager.
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.ui = booking_window()
        self.ui.setupUi(self)

        self.show()
