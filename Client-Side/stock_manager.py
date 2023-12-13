"""
This file  contains the StockManager class which runs and controls inputs to and from
the stock management window.
"""

import global_vars

from PyQt5 import QtWidgets as qtw

from Ui.StockWindow import Ui_StockManager as stock_window

class StockManager(qtw.QMainWindow):
    """
    This class handles all interactions with the stock manager.
    """

    def __init__(self, parent=None):

        if not global_vars.LOGGED_IN or global_vars.PRIORITY < 2:
            return

        super().__init__(parent=parent)

        self.ui = stock_window()
        self.ui.setupUi(self)

        self.stock = global_vars.CONNECTION_MANAGER.send_command("SELECT * FROM STOCK")
        self.suppliers = global_vars.CONNECTION_MANAGER.send_command("SELECT * FROM SUPPLIER")

        print(self.stock, self.suppliers)

        self.fill_stock()
        self.connect_buttons()

        self.show()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend of the booking manager
        to their respective functions.
        """
        self.ui.add_stock.clicked.connect(self.test)
        self.ui.remove.clicked.connect(self.test)
        self.ui.update.clicked.connect(self.test)

    def fill_stock(self):
        """
        This procedure fills in the frontend QScroll area with all of the current
        stock in the database.
        """
        for stock_item in self.stock:
            print(f"Item: {stock_item[1]}\n\
Amount:{stock_item[2]}\n\
Price: £{stock_item[3]/100}\n\
From: {stock_item[4]}")

    def test(self):
        """
        A test function to show button clicks.
        """
        print("Worked!")
