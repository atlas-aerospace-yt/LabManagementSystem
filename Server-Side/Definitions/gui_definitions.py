"""
This file holds the definitions for the GUI including
HTML beginning and end tags, and user prompts.
"""

MSG_LOGIN = """<h1><p style=\"color:#fc7303\">Terminal</p></h1>
<p style=\"color:#000000\">Please enter the admin password!<br></p>
"""

GET_PWD_HASH = """SELECT PasswordHash FROM INSTITUTION"""

MSG_INSTRUCTIONS = """<h1><p style=\"color:#fc7303\">Terminal</p></h1><p style=\"color:#000000\">
The options for the admin terminal are:<br>
\"disconnect\" [-a] - disconect all users e.g. \"disconnect-a\"<br>
\"disconnect\" [-ip-port] - disconnect a specific user e.g. \"disconnect-127.0.0.1-5555\"<br>
\"SQL\" [-sql] - run an SQL command on the server e.g. \"SQL-SELECT * FROM MY_TABLE\"<br>
\"reset\" [-password] - change the administrator password e.g. \"reset-12345\"<br>
\"info\" - to get information about the activity<br>
\"clear\" - clear all of the information shown in the terminal<br>
\"logout\" - log out of the admin terminal<br>
\"exit\" - ends the server side program</p>"""

MSG_BEGINNING = "<p style=\"color:#fc7303\">>>> <font color=\"#000000\">"
MSG_ENDING = "</P>"

COMMAND_KEY_WORDS = ["info", "disconnect"]

INVALID_PASSWORD = "Invalid password!"

RESET_PASSWORD_SUCC = "Your new password has been set."
RESET_PASSWORD_FAIL = "Please enter a password longer than 4 characters."

DISCONNECT_ALL = "Disconnected all users."

EXIT = "exit"
SQL = "sql"
RESET = "reset"
LOGOUT = "logout"
INFO = "info"
CLEAR = "clear"
DISCONNECT = "disconnect"
