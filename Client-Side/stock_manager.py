"""
This file  contains the StockManager class which runs and controls inputs to and from
the stock management window. It also holds the AddingStock class which the StockManager
uses when the user adds a new stock item.
"""

import re

import global_vars
import Definitions.sql_definitions as sql
import Definitions.gui_definitions as gui

from PyQt5 import QtWidgets as qtw

from Ui.StockWindow import Ui_StockManager as stock_window
from Ui.AddStockWindow import Ui_AddStock as add_stock_window

stock = global_vars.CONNECTION_MANAGER.send_command(sql.GET_STOCK_AND_SUPPLIER)

class AddingStock(qtw.QMainWindow):
    """
    This class adds stock based off of the users inputs.
    """

    def __init__(self, parent=None):
        # No condition here as they will have already opened StockManager
        super().__init__(parent=parent)

        self.ui = add_stock_window()
        self.ui.setupUi(self)

        self.connect_buttons()

        self.show()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend of the booking manager
        to their respective functions.
        """
        self.ui.addstock.clicked.connect(self.add_stock)

    def add_stock(self):
        """
        Add the stock to the database.
        """
        name = self.ui.name.text()
        amount = self.ui.amount.text()
        price = self.ui.price.text()
        website = self.ui.website.text()
        supplier_name = self.ui.supplier_name.text()
        phone = self.ui.phone.text()
        email = self.ui.email.text()

        # Check all of the data input is valid
        if not amount.isnumeric() or not price.isnumeric():
            return
        if not (name and amount and price and website and supplier_name and phone and email):
            return

        # Add the stock item. TODO


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
        self.stock_indeces = []
        self.last_search = sql.GET_STOCK_AND_SUPPLIER

        self.stock = global_vars.CONNECTION_MANAGER.send_command(sql.GET_STOCK_AND_SUPPLIER)

        self.fill_stock()
        self.connect_buttons()

        self.show()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend of the booking manager
        to their respective functions.
        """
        self.ui.add_stock.clicked.connect(self.show_add_stock)
        self.ui.remove.clicked.connect(self.remove_stock)
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
            query = sql.GET_STOCK_AND_SUPPLIER + f" WHERE {sql.STOCK_AND_SUPPLIER_VARS[0]} \
LIKE \"%{search_term}%\" "
            for col in sql.STOCK_AND_SUPPLIER_VARS[1:]:
                query += f"OR {col} LIKE \"%{search_term}%\" "

        self.last_search = query
        self.stock = global_vars.CONNECTION_MANAGER.send_command(query)

        self.ui.name.setText("")
        self.stock_widgets = []

        self.fill_stock()

    def add_stock_button(self, string, indx=None, pos=-1):
        """
        Add a new stock button to the screen to show the stock in the database.
        
        Args:
            string(str): the string to tell the user what stock is in the database
            pos(int): the index of the next button
        """
        self.stock_indeces.append(indx)
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
        self.selected = -1
        while self.ui.stock_view.count():
            child = self.ui.stock_view.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.stock_indeces = []

        if len(self.stock) == 0:
            self.add_stock_button("\n\nNO STOCK\n\n")
            return

        for stock_item in self.stock:
            indx = stock_item[0]

            string = f"Item: {stock_item[1]}\n\
Amount:{stock_item[2]}\n\
Price: £{stock_item[3]/100}\n\
From: {stock_item[4]}\n\
Supplier: {stock_item[5]}\n\
Email: {stock_item[6]}\n\
Phone: {stock_item[7]}"

            self.add_stock_button(string, indx, len(self.stock_widgets))

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
        # Update the amount of stock
        amount = self.ui.amount.text()
        indx = self.stock_indeces[self.selected]

        if not amount.isnumeric() or self.selected == -1:
            return

        global_vars.CONNECTION_MANAGER.send_command(
            f"UPDATE STOCK SET Amount={amount} WHERE StockID={indx}")

        self.ui.amount.setText("")

        # Update displayed stock.
        self.stock_widgets = []
        self.stock = global_vars.CONNECTION_MANAGER.send_command(self.last_search)
        self.fill_stock()

    def remove_stock(self):
        """
        Remove the stock item which is selected and make the user confirm with a QtMessageBox.
        
        The QMessageBox code is inspired by: https://www.geeksforgeeks.org/pyqt5-message-box/
        """
        # Confirm the selection with a warning window.
        warning = qtw.QMessageBox()
        warning.setIcon(qtw.QMessageBox.Warning)
        warning.setText("Warning - this will delete the selected stock and cannot be undone!")
        warning.setWindowTitle("Warning")
        warning.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        output = warning.exec_()

        # ONLY if the click "OK" proceed.
        if output != qtw.QMessageBox.Ok:
            return

        # Delete stock item.
        indx = self.stock_indeces[self.selected]

        global_vars.CONNECTION_MANAGER.send_command(f"DELETE FROM STOCK WHERE StockID={indx}")

        # Update displayed stock.
        self.stock_widgets = []
        self.stock = global_vars.CONNECTION_MANAGER.send_command(sql.GET_STOCK_AND_SUPPLIER)
        self.fill_stock()

    def show_add_stock(self):
        """
        Allow the user to add a new stock item by opening the add stock window.
        """
        AddingStock(self)
