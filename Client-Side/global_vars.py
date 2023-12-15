"""
Global variables that can change are defined here.
"""

from connection_manager import ConnectionManager

try:
    CONNECTION_MANAGER = ConnectionManager()
except ConnectionRefusedError:
    CONNECTION_MANAGER = None

USER_ID = None
USER_EMAIL = None
LOGGED_IN = False

PRIORITY = -1
