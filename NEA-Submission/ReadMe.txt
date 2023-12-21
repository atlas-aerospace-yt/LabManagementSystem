ABSTRACT:

This release is a very limited demonstration of the functionallity of this open-sourced laboratory management system.


ACCOUNT(S) INFORMATION:

This will allow you to experience the app as three different kinds of users:
Admin------------email: admin-------password: 12345
Sixthformer------email: sixthform---password: 12345
Student----------email: student-----password: 12345

The admin terminal password is: 12345


INSTRUCTIONS:

This app proof-of-concept release should allow you to create bookings, add stock, remove stock, edit stock, and graph data. To run the example release, run the server-side main.py before running the client-side main.py. Then run the client-side main.py for every client you want to simulate. Each client is its' own instance of the application and will act as if they were connected over a network.

To run the raw python, you must install all of the pip libraries that are in the requirements.txt, alternatively you can use the command: "pip install -r requirements.txt".

If there are any questions or queries please email me.

To manage stock, you must be logged in as admin.
To book a lab, you must be logged in as admin/sixthformer.

WARNINGS:

THE APP DOES NOT RESPOND WHILE COMMITTING DATA THIS BUG IS KNOW, DO NOT CLOSE APP WHILE NOT RESPONDING!

THE EMAIL NOTIFICATIONS FOR THIS APP HAVE BEEN REMOVED AS THAT WOULD INVOLVE SHARING MY EMAIL TO THE INTERNET, THIS FEATURE DOES WORK AND HAS BEEN TESTED.

THIS APP WILL RUNNING USING LOCAL HOST.