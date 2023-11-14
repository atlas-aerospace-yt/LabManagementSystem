"""
This file holds the definitions for the GUI including
HTML beginning and end tags, and user prompts.
"""

MSG_LOGIN = """<h1><p style=\"color:#fc7303\">Terminal</p></h1>
<p style=\"color:#000000\">Please enter the admin password!<br></p>
"""

GET_PWD_HASH = """SELECT PasswordHash FROM INSTITUTION"""

MSG_INSTRUCTIONS = """<h1><p style=\"color:#fc7303\">Terminal</p></h1>
<p style=\"color:#000000\">The options for the admin terminal are:<br>
\"exit\" - ends the server side program<br>
\"SQL\"(command) - run an SQL command on the servers<br>
\"info\" - to get information about the activity<br>
\"disconnect\" - (all or ip) - disconects a specific user or all.<br>
\"reset\"(password) - change the administrator password</p>"""

MSG_BEGINNING = "<p style=\"color:#fc7303\">>>> <font color=\"#000000\">"
MSG_ENDING = "</P>"

COMMAND_KEY_WORDS = ["info", "disconnect"]
