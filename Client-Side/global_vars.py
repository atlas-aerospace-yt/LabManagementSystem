"""
Global variables that can change are defined here.
"""

from PyQt5 import QtWidgets as qtw
from connection_manager import ConnectionManager

try:
    CONNECTION_MANAGER = ConnectionManager()
except ConnectionRefusedError:
    error = qtw.QMessageBox.critical(None,
                                        "Startup Error", 
                                        "Could not connect to the server!",
                                        qtw.QMessageBox.Cancel)

USER_ID = None
USER_EMAIL = None
LOGGED_IN = False

PRIORITY = -1
