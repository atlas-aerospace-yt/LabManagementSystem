"""
This file  contains the StockManager class which runs and controls inputs to and from
the stock management window.
"""

import re

import global_vars
import Definitions.sql_definitions as sql
import Definitions.gui_definitions as gui

from PyQt5 import QtWidgets as qtw

from Ui.StockWindow import Ui_StockManager as stock_window

stock = global_vars.CONNECTION_MANAGER.send_command(sql.GET_STOCK_AND_SUPPLIER)

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

        self.selected = -1
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
        self.ui.update.clicked.connect(self.update_amount)
        self.ui.name.returnPressed.connect(self.search_for_stock)
        self.ui.amount.returnPressed.connect(self.update_amount)

    def search_for_stock(self):
        """
        Display stock that is only relevant to what the user has searched for then re-update
        the stock shown on the frontend to the user.
        """
        search_term = self.ui.name.text().replace("\"", "")
        search_term = re.sub(r"(?<=\d).(?=\d)", "", search_term)
        search_term = re.sub(r"£(?=\d)", "", search_term)

        if search_term == "":
            query = sql.GET_STOCK_AND_SUPPLIER
        else:
            query = sql.GET_STOCK_AND_SUPPLIER + f" WHERE {sql.STOCK_AND_SUPPLIER_VARS[0]}\
LIKE \"%{search_term}%\" "
            for col in sql.STOCK_AND_SUPPLIER_VARS[1:]:
                query += f"OR {col} LIKE \"%{search_term}%\" "
            print(query)
        self.stock = global_vars.CONNECTION_MANAGER.send_command(query)

        self.ui.name.setText("")
        self.stock_widgets = []

        self.fill_stock()

    def add_stock_button(self, string, pos=-1):
        """
        Add a new stock button to the screen to show the stock in the database.
        
        Args:
            string(str): the string to tell the user what stock is in the database
            pos(int): the index of the next button
        """
        self.stock_widgets.append(qtw.QPushButton(string))
        self.stock_widgets[pos].setStyleSheet(gui.STYLESHEET)
        if pos != -1:
            self.stock_widgets[pos].clicked.connect(lambda: self.update_selected(pos))
        self.ui.stock_view.addWidget(self.stock_widgets[pos])

    def fill_stock(self):
        """
        This procedure fills in the frontend QScroll area with all of the current
        stock in the database.
        """
        while self.ui.stock_view.count():
            child = self.ui.stock_view.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.stock_widget = []

        if len(self.stock) == 0:
            self.add_stock_button("\n\nNO STOCK\n\n")
            return

        for stock_item in self.stock:

            string = f"Item: {stock_item[0]}\n\
Amount:{stock_item[1]}\n\
Price: £{stock_item[2]/100}\n\
From: {stock_item[3]}\n\
Supplier: {stock_item[4]}\n\
Email: {stock_item[5]}\n\
Phone: {stock_item[6]}"

            self.add_stock_button(string, len(self.stock_widgets))

    def update_selected(self, indx):
        """
        Change the selected button.

        Args:
            indx(int): the button that has been selected.
        """
        if indx == self.selected:
            for item in self.stock_widgets:
                item.setStyleSheet(gui.STYLESHEET)
            self.selected = -1
        else:
            for item in self.stock_widgets:
                item.setStyleSheet(gui.STYLESHEET)
            self.stock_widgets[indx].setStyleSheet(gui.SELECTED_STYLESHEET)
            self.selected = indx

    def update_amount(self):
        """
        Update the amount of stock that is stored in the database.
        """
        amount = self.ui.amount.text()

        if not amount.isnumeric():
            return

        print(amount)
        self.ui.amount.setText("")

    def test(self):
        """
        A test function to show button clicks.
        """
        print("Worked!")
