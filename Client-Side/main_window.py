"""
This file holds the class which runs the home screen for the
Lab Management system.
"""

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

import Definitions.gui_definitions as gui
import Definitions.sql_definitions as sql

from Ui.MainWindow import Ui_MainWindow as main_window
from graph_manager import GraphManager

class MainUI(qtw.QMainWindow):
    """
    This class handles all user interactions with the main window.
    """

    def __init__(self, connection_manager):
        super().__init__()

        self.ui = main_window()

        self.time_table_widgets = []
        self.connection_manager = connection_manager

        self.ui.setupUi(self)
        self.connect_buttons()
        self.fill_in_timetable()

        print(self.connection_manager.send_command(sql.GET_BOOKINGS_INFO))
        timer = qtc.QTimer(self)
        timer.setInterval(25)
        timer.timeout.connect(self.update_display)
        timer.start()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend to the rest
        of the code.
        """
        self.ui.account.clicked.connect(self.test)
        self.ui.help.clicked.connect(self.test)
        self.ui.log_experiment.clicked.connect(self.open_graph_window)
        self.ui.manage_stock.clicked.connect(self.test)

    def add_widget_to_timetable(self, text, pos_i, pos_j , stylesheet="", scale=False):
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
        self.time_table_widgets[pos_i].append(qtw.QPushButton(text))
        self.time_table_widgets[pos_i][pos_j].setStyleSheet(stylesheet)
        self.time_table_widgets[pos_i][pos_j].clicked.connect(self.test)
        self.ui.time_table.addWidget(self.time_table_widgets[pos_i][pos_j], pos_i, pos_j)

        if not scale:
            self.time_table_widgets[pos_i][pos_j].setMinimumHeight(50)

    def fill_in_timetable(self):
        """
        Fill in the timetable with the correct information.
        """
        times = self.connection_manager.send_command("SELECT * FROM TIMETABLE")
        for i in range(len(times)):
            for j in range(1, len(times[i])):
                time_seconds = times[i][j]
                time = time_seconds.split(":")[:-1]
                output = time[0] + ":" + time[1]
                times[i][j] = output

        for i in range(len(times)+1):
            self.time_table_widgets.append([])
            for j in range(gui.NUM_OF_COLS):
                if i == 0 and j == 0:
                    self.add_widget_to_timetable("TimeTable", i, j, gui.TITLE_CSS)
                    continue
                elif i == 0:
                    self.add_widget_to_timetable(gui.DAYS_OF_THE_WEEK[j-1], i, j, gui.TITLE_CSS)
                    continue
                elif j == 0:
                    self.add_widget_to_timetable(
                        f"{times[i-1][1]}-{times[i-1][2]}", i, j, gui.TITLE_CSS)
                    continue

                self.add_widget_to_timetable(f"QPushButton at: \n\n\n\n\n\n{i}, {j}", i, j, gui.STANDARD_CSS, True)

    def update_display(self):
        """
        Get the data from the database and display the booked slots.
        """
        pass

    def test(self):
        """
        Test button clicks.
        """
        print("Worked")

    def open_graph_window(self):
        """
        Open the graph window so that they can log experiments.
        """
        GraphManager(self)
