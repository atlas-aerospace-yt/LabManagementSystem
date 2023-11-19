"""
This file holds the class which runs the home screen for the
Lab Management system.
"""

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from Ui.MainWindow import Ui_MainWindow as main_window

class MainUI(qtw.QMainWindow):
    """
    This class handles all user interactions with the main window.
    """

    def __init__(self):
        super().__init__()

        self.ui = main_window()

        self.time_table_widgets = []

        self.ui.setupUi(self)
        self.connect_buttons()
        self.fill_in_timetable()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend to the rest
        of the code.
        """
        self.ui.account.clicked.connect(self.test)
        self.ui.help.clicked.connect(self.test)
        self.ui.log_experiment.clicked.connect(self.test)
        self.ui.manage_stock.clicked.connect(self.test)

    def fill_in_timetable(self):
        """
        Uses some code from:
        https://realpython.com/python-pyqt-layout/#arranging-widgets-in-a-grid-qgridlayout
        """

        for i in range(8):
            self.time_table_widgets.append([])
            for j in range(8):
                self.time_table_widgets[i].append(qtw.QPushButton(f"Button at: {i}, {j}"))
                self.time_table_widgets[i][j].setMinimumHeight(50)
                self.ui.time_table.addWidget(self.time_table_widgets[i][j], i, j)

    def test(self):
        """
        Test button clicks.
        """
        print("Worked")
