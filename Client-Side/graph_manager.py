"""
This file holds the GraphManager class which allows the user to pass in data.
"""

import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

import Definitions.graph_definitions as graph
from Ui.GraphPlotter import Ui_GraphWindow as graph_plotter

class GraphManager(qtw.QMainWindow):
    """
    This class handles all of the data input and output via the
    Graph plotting window.
    """

    def __init__(self):
        super().__init__()

        self.ui = graph_plotter()

        self.x_co_ordinates = []
        self.y_co_ordinates = []

        self.status = 1

        self.ui.setupUi(self)
        self.connect_buttons()

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

    def display_messsage(self):
        """
        Each frame, update the list shown in the QTextBrowser. This is so that the user
        can see data that they have iput.
        """

        if not self.status:
            return

        message = graph.MSG_TITLE
        for x_value, y_value in zip(self.x_co_ordinates, self.y_co_ordinates):
            message += f"{graph.MSG_BEGINNING} {x_value}, {y_value}{graph.MSG_ENDING}"
        self.ui.data.setHtml(message)

        self.status = 0

    def verify_data(self, x_co_ordinare:str, y_co_ordinate:str) -> bool:
        """
        Verify the x and y coordingate that have been input and that the data is
        numerical even if it is negative (has "-") or a decimal (has ".").

        Args:
            x_co_ordinate(str): the x co-ordinare value the user has input
            y_co_ordinate(str): the y co-ordinate value the user has input

        Returns:
            bool: if the data is valid or not
        """
        integer_x = x_co_ordinare.replace(".","").replace("-","")
        integer_y = y_co_ordinate.replace(".","").replace("-","")

        print(integer_x.isnumeric(), integer_y.isnumeric())
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
        """

        x = np.array(self.x_co_ordinates, dtype=np.float64)
        y = np.array(self.y_co_ordinates, dtype=np.float64)
        gradient, intercept = np.polyfit(x, y, 1)
        plt.scatter(x, y)
        plt.plot(x, gradient * x + intercept)
        plt.show()
