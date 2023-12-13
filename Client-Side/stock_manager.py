"""
This file  contains the StockManager class which runs and controls inputs to and from
the stock management window.
"""

import global_vars
import Definitions.sql_definitions as sql
import Definitions.gui_definitions as gui

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

        self.stock_widgets = []
        self.stock = global_vars.CONNECTION_MANAGER.send_command(sql.GET_STOCK_AND_SUPPLIER)

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
        stock_strings = []
        for stock_item in self.stock:

            stock_strings.append(f"Item: {stock_item[0]}\n\
Amount:{stock_item[1]}\n\
Price: £{stock_item[2]/100}\n\
From: {stock_item[3]}\n\
Supplier: {stock_item[4]}\n\
Email: {stock_item[5]}\n\
Phone: {stock_item[6]}")

        for string in stock_strings:
            indx = len(self.stock_widgets)
            self.stock_widgets.append(qtw.QPushButton(string))
            self.stock_widgets[-1].setStyleSheet(gui.STYLESHEET)
            self.stock_widgets[-1].clicked.connect(lambda: self.update_selected(indx))
            self.ui.stock_view.addWidget(self.stock_widgets[-1])

    def update_selected(self, indx):
        """
        Change the selected button.

        Args:
            indx(int): the button that has been selected.
        """
        print(f"COCK FUCKER {indx}")

    def test(self):
        """
        A test function to show button clicks.
        """
        print("Worked!")
