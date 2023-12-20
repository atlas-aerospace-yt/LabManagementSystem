# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ServerSide.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 424)
        MainWindow.setStyleSheet("/*General Styling*/\n"
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
"    background: #ffffff;\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line \n"
"{\n"
"    background: #ffffff;\n"
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
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.num_of_connections = QtWidgets.QLabel(self.centralwidget)
        self.num_of_connections.setMinimumSize(QtCore.QSize(250, 40))
        self.num_of_connections.setAlignment(QtCore.Qt.AlignCenter)
        self.num_of_connections.setObjectName("num_of_connections")
        self.gridLayout.addWidget(self.num_of_connections, 0, 1, 1, 2)
        self.command = QtWidgets.QLineEdit(self.centralwidget)
        self.command.setMinimumSize(QtCore.QSize(0, 40))
        self.command.setObjectName("command")
        self.gridLayout.addWidget(self.command, 2, 1, 1, 2)
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setStyleSheet("* {\n"
"\n"
"    background-color: #ffffff;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.terminal = QtWidgets.QTextBrowser(self.gridWidget)
        self.terminal.setMinimumSize(QtCore.QSize(200, 150))
        self.terminal.setObjectName("terminal")
        self.gridLayout_3.addWidget(self.terminal, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.gridWidget, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server Side"))
        self.num_of_connections.setText(_translate("MainWindow", "Connections: 0"))
        self.command.setPlaceholderText(_translate("MainWindow", "Please enter command here."))
        self.terminal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
