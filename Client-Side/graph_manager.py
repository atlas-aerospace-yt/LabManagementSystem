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

        self.ui.setupUi(self)

    def connect_buttons(self):
        """
        Connect all of the buttons from the frontend to the rest
        of the code.
        """
        pass

    def verify_data(self):
        """
        Verify the graph data that the user has entered into the
        front end.
        """
        pass
