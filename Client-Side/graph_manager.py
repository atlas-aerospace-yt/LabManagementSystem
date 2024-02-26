"""
This file holds the GraphManager class which allows the user to pass in data.
"""

import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

import Definitions.gui_definitions as gui
from Ui.GraphPlotter import Ui_GraphWindow as graph_plotter

class GraphManager(qtw.QMainWindow):
    """
    This class handles all of the data input and output via the
    Graph plotting window.
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.ui = graph_plotter()

        self.x_co_ordinates = []
        self.y_co_ordinates = []

        self.status = 1

        self.ui.setupUi(self)
        self.connect_buttons()

        self.show()

        timer = qtc.QTimer(self)
        timer.setInterval(25)
        timer.timeout.connect(self.display_messsage)
        timer.start()

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend to the rest
        of the code.
        """
        self.ui.add_variable.clicked.connect(self.append_graph_data)
        self.ui.plot_graph.clicked.connect(self.create_graph)
        self.ui.clear_data.clicked.connect(self.clear_data)

    def display_messsage(self):
        """
        Each frame, update the list shown in the QTextBrowser. This is so that the user
        can see data that they have iput.
        """

        if not self.status:
            return

        message = gui.GRAPH_MSG_TITLE
        for x_value, y_value in zip(self.x_co_ordinates, self.y_co_ordinates):
            message += f"{gui.GRAPH_MSG_BEGINNING} {x_value}, {y_value}{gui.GRAPH_MSG_ENDING}"
        self.ui.data.setHtml(message)

        self.status = 0

    def clear_data(self):
        """
        Clear all data when the user is done with one graph so that they can add another.
        """
        self.x_co_ordinates = []
        self.y_co_ordinates = []
        self.status = 1

    def verify_data(self, x_co_ordinate:str, y_co_ordinate:str) -> bool:
        """
        Verify the x and y coordingate that have been input and that the data is
        numerical even if it is negative (has "-") or a decimal (has ".").

        Args:
            x_co_ordinate(str): the x co-ordinare value the user has input
            y_co_ordinate(str): the y co-ordinate value the user has input

        Returns:
            bool: if the data is valid or not
        """

        if x_co_ordinate.count(".") > 1 or y_co_ordinate.count(".") > 1:
            return False

        integer_x = x_co_ordinate.replace(".","").replace("-","")
        integer_y = y_co_ordinate.replace(".","").replace("-","")

        if integer_x.isnumeric() and integer_y.isnumeric():
            return True
        return False

    def append_graph_data(self):
        """
        Verify the graph data that the user has entered into the
        front end.
        """
        x_data = self.ui.x_variable.text()
        y_data = self.ui.y_variable.text()

        if not self.verify_data(x_data, y_data):
            self.ui.notification.setText("The data is invalid!")
            return

        self.ui.x_variable.setText("")
        self.ui.y_variable.setText("")
        self.ui.notification.setText("")

        self.x_co_ordinates.append(x_data)
        self.y_co_ordinates.append(y_data)
        self.status = 1

    def create_graph(self):
        """
        This displays the graph in a matplotlib.pyplot for the user to see and interact
        with as they wish.
        The line of best fit followed this tutorial: https://www.statology.org/line-of-best-fit-python/.
        """

        x = np.array(self.x_co_ordinates, dtype=np.float64)
        y = np.array(self.y_co_ordinates, dtype=np.float64)
        gradient, intercept = np.polyfit(x, y, 1)
        plt.scatter(x, y)
        plt.plot(x, gradient * x + intercept)
        plt.show()
