# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\StockWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StockManager(object):
    def setupUi(self, StockManager):
        StockManager.setObjectName("StockManager")
        StockManager.resize(600, 380)
        StockManager.setStyleSheet("/*General Styling*/\n"
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
"    width:10px;\n"
"    border: none;\n"
"    background: #0388fc;\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page \n"
"{\n"
"    background: #0388fc;\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line \n"
"{\n"
"    background: #0388fc;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"    background-color: #fc7303;\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
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
"\n"
"/* Remove border */\n"
"QScrollArea {\n"
"    border:none;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(StockManager)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.amount.setMinimumSize(QtCore.QSize(0, 50))
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 3, 0, 1, 1)
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setMinimumSize(QtCore.QSize(0, 50))
        self.update.setObjectName("update")
        self.gridLayout.addWidget(self.update, 4, 0, 1, 1)
        self.add_stock = QtWidgets.QPushButton(self.centralwidget)
        self.add_stock.setMinimumSize(QtCore.QSize(0, 50))
        self.add_stock.setObjectName("add_stock")
        self.gridLayout.addWidget(self.add_stock, 1, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setMinimumSize(QtCore.QSize(0, 50))
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 383, 282))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stock_view = QtWidgets.QGridLayout()
        self.stock_view.setObjectName("stock_view")
        self.gridLayout_4.addLayout(self.stock_view, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 1, 7, 1)
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setMinimumSize(QtCore.QSize(0, 50))
        self.remove.setObjectName("remove")
        self.gridLayout.addWidget(self.remove, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        StockManager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StockManager)
        self.statusbar.setObjectName("statusbar")
        StockManager.setStatusBar(self.statusbar)

        self.retranslateUi(StockManager)
        QtCore.QMetaObject.connectSlotsByName(StockManager)

    def retranslateUi(self, StockManager):
        _translate = QtCore.QCoreApplication.translate
        StockManager.setWindowTitle(_translate("StockManager", "MainWindow"))
        self.amount.setPlaceholderText(_translate("StockManager", "Enter amount"))
        self.update.setText(_translate("StockManager", "Update"))
        self.add_stock.setText(_translate("StockManager", "Add new stock item"))
        self.name.setPlaceholderText(_translate("StockManager", "Search for stock"))
        self.remove.setText(_translate("StockManager", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StockManager = QtWidgets.QMainWindow()
    ui = Ui_StockManager()
    ui.setupUi(StockManager)
    StockManager.show()
    sys.exit(app.exec_())
