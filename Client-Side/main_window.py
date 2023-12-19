"""
This file holds the class which runs the home screen for the
Lab Management system.
"""

# Python PIP libraries see requirements.txt for more
from datetime import datetime, timedelta

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from Ui.MainWindow import Ui_MainWindow as main_window

# Custom libraries go here
import global_vars

import Definitions.gui_definitions as gui
import Definitions.sql_definitions as sql

from graph_manager import GraphManager
from booking_manager import BookingManager
from account_manager import AccountManager
from stock_manager import StockManager

class MainUI(qtw.QMainWindow):
    """
    This class handles all user interactions with the main window.
    """

    def __init__(self):
        super().__init__()

        self.ui = main_window()

        self.time_table_widgets = []
        self.bookings = {}

        self.ui.setupUi(self)

        # Get dates to fill in the QComboBox
        today = datetime.now()
        last_monday = today - timedelta(days=(today.weekday() - 0)%7)
        for i in range(gui.DATE_RANGE):
            self.ui.date_range.addItem((last_monday + timedelta(weeks=i)).strftime("%d-%m-%Y"))

        # Get all of the bookable labs
        self.labs = global_vars.CONNECTION_MANAGER.send_command(sql.GET_LABS)

        # Get all of the time slots
        self.times = global_vars.CONNECTION_MANAGER.send_command("SELECT * FROM TIMETABLE")

        self.connect_buttons()
        self.fill_in_timetable()

        # Two seperate timers, one to update the data on display every minute, one to
        # constantly check for a valid connection to the server.
        self.update_display()
        timer = qtc.QTimer(self)
        timer.setInterval(60000)
        timer.timeout.connect(self.update_display)
        timer.start()

        timer = qtc.QTimer(self)
        timer.setInterval(0)
        timer.timeout.connect(self.check_connection)
        timer.start()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend to the rest
        of the code.
        """
        self.ui.account.clicked.connect(self.open_account_window)
        self.ui.help.clicked.connect(self.test)
        self.ui.log_experiment.clicked.connect(self.open_graph_window)
        self.ui.manage_stock.clicked.connect(self.open_stock_window)
        self.ui.date_range.activated[str].connect(self.update_display)

    def add_widget_to_timetable(self, text, pos, stylesheet="", scale=False):
        """
        Add a widget to the timetable grid on the front of the screen.

        Uses some code from:
        https://realpython.com/python-pyqt-layout/#arranging-widgets-in-a-grid-qgridlayout

        Args:
            text(str): the text to put on the QTextBrowser
            pos_i(int): the row to put the widget in
            pos_j(int): the column to put the widget in
            stylesheet(str): the css to style the QTextBrowser
        """
        self.time_table_widgets[pos[0]].append(qtw.QPushButton(text))
        self.time_table_widgets[pos[0]][pos[1]].setStyleSheet(stylesheet)
        self.time_table_widgets[pos[0]][pos[1]].clicked.connect(
            lambda: self.open_booking_window(pos[0], pos[1]))
        self.time_table_widgets[pos[0]][pos[1]].setSizePolicy(
            qtw.QSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding))
        self.ui.time_table.addWidget(self.time_table_widgets[pos[0]][pos[1]], pos[0], pos[1])

        if not scale:
            self.time_table_widgets[pos[0]][pos[1]].setMinimumHeight(50)

    def format_time(self, time_hh_mm_ss:str):
        """
        Takes in the time in the format hh:mm:ss and puts it into the format
        of hh:mm.

        Args:
            time_hh_mm_ss(str): the time in hh:mm:ss format

        Returns:
            str: the time in hh:mm format
        """
        time_list = time_hh_mm_ss.split(":")[:-1]
        output = time_list[0] + ":" + time_list[1]
        return output

    def fill_in_timetable(self):
        """
        Fill in the timetable with the correct information.
        """

        for i, _ in enumerate(self.times):
            for j in range(1, len(self.times[i])):
                self.times[i][j] = self.format_time(self.times[i][j])

        for i in range(len(self.times)+1):
            self.time_table_widgets.append([])
            for j in range(gui.NUM_OF_COLS):
                if i == 0 and j == 0:
                    self.add_widget_to_timetable("TimeTable", (i, j), gui.TITLE_CSS)
                elif i == 0:
                    self.add_widget_to_timetable(gui.DAYS_OF_THE_WEEK[j-1], (i, j), gui.TITLE_CSS)
                elif j == 0:
                    self.add_widget_to_timetable(
                        f"{self.times[i-1][1]}-{self.times[i-1][2]}", (i, j), gui.TITLE_CSS)
                else:
                    self.add_widget_to_timetable("", (i, j), gui.PLAIN_CSS, True)

    def get_data_to_update_display(self):
        """
        Get the data from the database and display the booked slots.
        To speed up the application, only the dates between the date range are selected from
        the database, the code for this was from:
        https://stackoverflow.com/questions/14208958/select-data-from-date-range-between-two-dates.

        Returns:
            list: The times shown on the timetable.
            list: The bookings that are in the database.
            list: The date range that is currently being displayed.
        """

        # Get a list of dates of the week
        this_monday = datetime.strptime(self.ui.date_range.currentText(), "%d-%m-%Y")
        date_range = []
        for i in range(7):
            date_range.append((this_monday + timedelta(days=i)).strftime("%d-%m-%Y"))

        # A list which has Forename, Surname, Subject, Date, StartTime, EndTime
        condition = f" WHERE (Date BETWEEN \"{date_range[0]}\" AND \"{date_range[-1]}\")"
        timetable = global_vars.CONNECTION_MANAGER.send_command(sql.GET_BOOKINGS_INFO + condition)

        if timetable is None:
            timetable = []

        # Get the list of times that are being displayed
        times = []
        for widget_list in self.time_table_widgets:
            times.append(widget_list[0].text())
        times.pop(0)

        return times, timetable, date_range

    def check_connection(self):
        """
        Verify the connection with the server and inform the user as quickly as possible if
        the connection is lost.
        """
        if not global_vars.CONNECTION_MANAGER.running:

            warning = qtw.QMessageBox()
            warning.setIcon(qtw.QMessageBox.Critical)
            warning.setText("Error - The connection to the server has been lost...")
            warning.setWindowTitle("Error")
            warning.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
            warning.exec_()

            self.close()

    def update_display(self):
        """
        Show all of the bookings on the timetable for the user to interact with.
        This works by first getting the time, timetable and daterange. Then bookings
        are added to a bookings dictionary which holds the names of the bookings and the
        lab which the booking is in. The co-ordinate of the booking on the timetable is
        the key for that dictionary item.
        """
        times, timetable, date_range = self.get_data_to_update_display()

        # Parse the bookings to add to the timetable
        self.bookings = {}
        for booking in timetable:
            string = f"\n{booking[0]}, {booking[1]}\n{booking[2]}\n"
            i = 1 + times.index(f"{self.format_time(booking[4])}-{self.format_time(booking[5])}")

            if booking[3] in date_range:
                j = 1 + date_range.index(booking[3])
            else:
                continue

            if (i,j) in self.bookings:
                self.bookings[(i,j)][0] += string
                self.bookings[(i,j)][1].append(booking[2])
            else:
                self.bookings[(i,j)] = [string, [booking[2]]]

        # Display the bookings to the users
        for i in range(1,len(times)+1):
            for j in range(1,8):
                if (i,j) in self.bookings and len(self.bookings[(i,j)][1]) < len(self.labs):
                    self.time_table_widgets[i][j].setText(self.bookings[(i,j)][0])
                    self.time_table_widgets[i][j].setStyleSheet(gui.BOOKED_CSS)
                elif (i,j) in self.bookings and len(self.bookings[(i,j)][1]) == len(self.labs):
                    self.time_table_widgets[i][j].setText(self.bookings[(i,j)][0])
                    self.time_table_widgets[i][j].setStyleSheet(gui.FULL_CSS)
                else:
                    self.time_table_widgets[i][j].setText("")
                    self.time_table_widgets[i][j].setStyleSheet(gui.PLAIN_CSS)

    def open_booking_window(self, i, j):
        """
        This function opens the booking window for the users to book stock.

        Args:
            i(int): the i index in self.timetable_widgets
            j(int): the j index in self.timetable_widgets
        """

        # Get a list of dates of the week
        this_monday = datetime.strptime(self.ui.date_range.currentText(), "%d-%m-%Y")
        date_range = []
        for day in range(7):
            date_range.append((this_monday + timedelta(days=day)).strftime("%d-%m-%Y"))

        days_into_week = (datetime.now()-this_monday).days + 1

        valid_time = 1 <= i <= len(self.time_table_widgets)
        valid_day = days_into_week < j <= len(self.time_table_widgets[0])

        if valid_time and valid_day:
            if (i,j) not in self.bookings:
                BookingManager(self.times[i-1], date_range[j-1], self.labs, self)
            elif len(self.bookings[(i,j)][1]) != len(self.labs):
                labs = []
                for lab in self.labs:
                    if lab[1] not in self.bookings[(i, j)][1]:
                        labs.append(lab)
                BookingManager(self.times[i-1], date_range[j-1], labs, self)

    def open_graph_window(self):
        """
        Open the graph window so that they can log experiments.
        """
        GraphManager(self)

    def open_account_window(self):
        """
        Open the account window so that the user can manage their account.
        """
        AccountManager(self)

    def open_stock_window(self):
        """
        Open the stock window so that the user can manage the stock.
        """
        StockManager(self)

    def test(self):
        """
        A test function to show button clicks.
        """
        print("Worked!")
