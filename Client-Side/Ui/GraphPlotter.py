# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GraphPlotter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(600, 370)
        GraphWindow.setMinimumSize(QtCore.QSize(600, 370))
        GraphWindow.setStyleSheet("/*General Styling*/\n"
"\n"
"* {\n"
"    font: 10pt \"Roboto\";\n"
"    font-size: 14px;\n"
"    line-height: 20px;\n"
"    background-color: #0388fc;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Text box styling*/\n"
"\n"
"QTextBrowser {\n"
"    border: none;\n"
"    padding-left:10px; \n"
"    padding-top:10px;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* Line edit styling */\n"
"QLineEdit {\n"
"    border: 10px;\n"
"    border-color: #fc7303;\n"
"    padding-left:10px; \n"
"    background-color: #FFFFFF;\n"
"    border-radius: 20px;\n"
"}\n"
"QLineEdit::hover {\n"
"    border: 5px solid;\n"
"    border-color: #fc7303;\n"
"}\n"
"\n"
"/* Label styling */\n"
"QLabel {\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    padding-left:10px; \n"
"    background-color: #FFFFFF;\n"
"    color: #fc7303;\n"
"    font-size: 30px;\n"
"}\n"
"\n"
"/* Scroll bar */\n"
"QScrollBar\n"
"{\n"
"    width: 20px;\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    background: #ffffff;\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page \n"
"{\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line \n"
"{\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"    background-color: #fc7303;\n"
"    min-height: 30px;\n"
"    border-radius: 10px;\n"
"    border:none;\n"
"}\n"
"QScrollBar::up-arrow\n"
"{\n"
"    background: none;\n"
"}\n"
"QScrollBar::down-arrow\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton::hover {\n"
"    border: 5px solid;\n"
"    border-color: #fc7303;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: #fc7303;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.notification = QtWidgets.QLabel(self.centralwidget)
        self.notification.setMinimumSize(QtCore.QSize(0, 50))
        self.notification.setText("")
        self.notification.setObjectName("notification")
        self.gridLayout.addWidget(self.notification, 11, 1, 1, 1)
        self.plot_graph = QtWidgets.QPushButton(self.centralwidget)
        self.plot_graph.setMinimumSize(QtCore.QSize(0, 50))
        self.plot_graph.setObjectName("plot_graph")
        self.gridLayout.addWidget(self.plot_graph, 11, 0, 1, 1)
        self.x_variable = QtWidgets.QLineEdit(self.centralwidget)
        self.x_variable.setMinimumSize(QtCore.QSize(0, 50))
        self.x_variable.setObjectName("x_variable")
        self.gridLayout.addWidget(self.x_variable, 2, 0, 1, 1)
        self.add_variable = QtWidgets.QPushButton(self.centralwidget)
        self.add_variable.setMinimumSize(QtCore.QSize(0, 50))
        self.add_variable.setObjectName("add_variable")
        self.gridLayout.addWidget(self.add_variable, 4, 0, 1, 1)
        self.data = QtWidgets.QTextBrowser(self.centralwidget)
        self.data.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.data.setObjectName("data")
        self.gridLayout.addWidget(self.data, 0, 1, 8, 1)
        self.clear_data = QtWidgets.QPushButton(self.centralwidget)
        self.clear_data.setMinimumSize(QtCore.QSize(0, 50))
        self.clear_data.setObjectName("clear_data")
        self.gridLayout.addWidget(self.clear_data, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.y_variable = QtWidgets.QLineEdit(self.centralwidget)
        self.y_variable.setMinimumSize(QtCore.QSize(0, 50))
        self.y_variable.setObjectName("y_variable")
        self.gridLayout.addWidget(self.y_variable, 3, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        GraphWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GraphWindow)
        self.statusbar.setObjectName("statusbar")
        GraphWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "Graph plotter"))
        self.plot_graph.setText(_translate("GraphWindow", "Plot graph"))
        self.x_variable.setPlaceholderText(_translate("GraphWindow", "Enter x co-ordinate"))
        self.add_variable.setText(_translate("GraphWindow", "Add variable"))
        self.clear_data.setText(_translate("GraphWindow", "Clear data"))
        self.y_variable.setPlaceholderText(_translate("GraphWindow", "Enter y co-ordinate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphWindow = QtWidgets.QMainWindow()
    ui = Ui_GraphWindow()
    ui.setupUi(GraphWindow)
    GraphWindow.show()
    sys.exit(app.exec_())
