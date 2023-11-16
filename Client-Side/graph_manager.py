"""
This file holds the GraphManager class.
"""

from PyQt5 import QtWidgets as qtw

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

        self.connect_buttons()

        self.ui.setupUi(self)

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend to the rest
        of the code.
        """
        self.ui.add_variable

    def append_graph_data(self):
        """
        Verify the graph data that the user has entered into the
        front end.
        """
        x_data = self.ui.x_variable.text()
        y_data = self.ui.y_variable.text()

        if x_data and y_data:
            print(x_data)
            print(y_data)
            self.ui.x_variable.setText("")
            self.ui.y_variable.setText("")
        else:
            print("Please fix inputs!")
