# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AccountWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AccountWindow(object):
    def setupUi(self, AccountWindow):
        AccountWindow.setObjectName("AccountWindow")
        AccountWindow.resize(699, 434)
        AccountWindow.setStyleSheet("/*General Styling*/\n"
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
        self.centralwidget = QtWidgets.QWidget(AccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setMinimumSize(QtCore.QSize(0, 50))
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setMinimumSize(QtCore.QSize(0, 50))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setMinimumSize(QtCore.QSize(0, 50))
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 2, 1, 1, 1)
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setMinimumSize(QtCore.QSize(0, 50))
        self.logout.setObjectName("logout")
        self.gridLayout.addWidget(self.logout, 7, 1, 1, 1)
        self.email_in = QtWidgets.QLineEdit(self.centralwidget)
        self.email_in.setMinimumSize(QtCore.QSize(0, 50))
        self.email_in.setObjectName("email_in")
        self.gridLayout.addWidget(self.email_in, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setMinimumSize(QtCore.QSize(0, 50))
        self.email.setText("")
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 3, 1, 1, 1)
        self.priority = QtWidgets.QLabel(self.centralwidget)
        self.priority.setMinimumSize(QtCore.QSize(0, 50))
        self.priority.setText("")
        self.priority.setAlignment(QtCore.Qt.AlignCenter)
        self.priority.setObjectName("priority")
        self.gridLayout.addWidget(self.priority, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 8)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        AccountWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AccountWindow)
        self.statusbar.setObjectName("statusbar")
        AccountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AccountWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountWindow)

    def retranslateUi(self, AccountWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountWindow.setWindowTitle(_translate("AccountWindow", "Account Manager"))
        self.login.setText(_translate("AccountWindow", "Log In"))
        self.password.setPlaceholderText(_translate("AccountWindow", "Enter password here."))
        self.logout.setText(_translate("AccountWindow", "Log Out"))
        self.email_in.setPlaceholderText(_translate("AccountWindow", "Enter email here."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountWindow = QtWidgets.QMainWindow()
    ui = Ui_AccountWindow()
    ui.setupUi(AccountWindow)
    AccountWindow.show()
    sys.exit(app.exec_())
