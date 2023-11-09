"""
This file contains the UserInterface class.    
"""

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from server_manager import ServerManager
from Ui.server_side import Ui_MainWindow as terminal

# Constant definitions TODO -> tidy up definition
MSG_INSTRUCTIONS = """<h1><p style=\"color:#fc7303\">Terminal</p></h1>
<p style=\"color:#000000\">The options for the admin terminal are:<br>
\"exit\" - ends the server side program<br>
\"SQL\"(command) - run an SQL command on the servers<br>
\"info\" - to get information about the activity<br>
\"disconnect\" - (all or ip) - disconects a specific user or all.<br></p>"""

MSG_BEGINNING = "<p style=\"color:#fc7303\">>>> <font color=\"#000000\">"
MSG_ENDING = "</P>"

COMMAND_KEY_WORDS = ["info", "disconnect"]

class UserInterface(qtw.QMainWindow):
    """
    Launches the server side terminal which is a GUI.

    Args:
        qtw (QtWidgets): the main window functions
    """

    def __init__(self):
        super().__init__()

        self.ui = terminal()
        self.server = ServerManager()

        self.message_attributes = [MSG_INSTRUCTIONS]
        self.prev_num_of_messages = 0

        self.ui.setupUi(self)
        self.connect_buttons()

        timer = qtc.QTimer(self)
        timer.setInterval(25)
        timer.timeout.connect(self.loop)
        timer.start()

    def connect_buttons(self):
        """
        Connects the enter key to the loop 
        """
        self.ui.command.returnPressed.connect(self.add_command)

    def loop(self):
        """
        Calls the main loop every 25ms.
        TODO -> Tidy up this function
        """
        # Loop the backend main loop
        self.server.main_loop()

        # Update the number of connections displayed on the screen
        connections = self.server.connection_manager.get_num_of_connection()
        self.ui.num_of_connections.setText(f"Connections: {connections}")

        # Add new results to the messages
        results = self.server.dequeue_admin_sql()
        results += self.server.dequeue_command()
        for result in reversed(results.split("\n")):
            if result:
                self.message_attributes.insert(1, result)

        if len(self.message_attributes) > self.prev_num_of_messages:
            self.update_html()
            self.prev_num_of_messages = len(self.message_attributes)

    def update_html(self):
        """
        Update the html being displayed.
        """
        html = self.message_attributes[0]
        for message in self.message_attributes[1:]:
            html += MSG_BEGINNING + message + MSG_ENDING
        self.ui.terminal.setHtml(html)

    def add_command(self):
        """
        Queues and parses the commands into the different types.
        TODO -> Tidy up this function
        """
        command = self.ui.command.text()

        valid = False

        if command.lower() == "exit":
            qtw.QCoreApplication.instance().quit()
            valid = True
        elif command[:3].lower() == "sql":
            # SQL is special as it joins a different queue.
            self.server.enqueue_sql(["admin", command[4:]])
            valid = True
        else:
            # Check for other commands.
            for key_word in COMMAND_KEY_WORDS:
                #print(command[:len(key_word)].lower(), key_word.lower())
                if command[:len(key_word)].lower() == key_word.lower():
                    self.server.enqueue_command(command[len(key_word)+1:])
                    valid = True

        if not valid:
            self.message_attributes.insert(1, "Invalid input: " + command)

        self.ui.command.setText("")

    def end(self):
        """
        Ends all connections to the database and to the client devices
        """
        self.server.database_manager.end_connection()
        self.server.connection_manager.end_server()
        self.server.connection_manager.end_connections()
