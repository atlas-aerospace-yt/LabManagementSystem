"""
A demo to fill the database.

https://learnsql.com/blog/how-to-join-3-tables-or-more-in-sql/
"""

FILL_USERS = [
"""INSERT INTO USERS VALUES(0, "Admin", "Account", "admin", "827ccb0eea8a706c4c34a16891f84e7b", 2);""",
"""INSERT INTO USERS VALUES(1, "SixthForm", "Account", "sixthform", "827ccb0eea8a706c4c34a16891f84e7b", 1);""",
"""INSERT INTO USERS VALUES(2, "Student", "Account", "student", "827ccb0eea8a706c4c34a16891f84e7b", 0);""",
]

FILL_LABS = [
"""INSERT INTO LABS VALUES(0, "Physics", "At the end of the science corridor.");""",
"""INSERT INTO LABS VALUES(1, "Chemistry", "The room before Physics.");""",
"""INSERT INTO LABS VALUES(2, "Biology", "Not a science.");""",
]

FILL_TIMETABLE = [
"""INSERT INTO TIMETABLE VALUES(1, "8:55:00", "9:55:00");""",
"""INSERT INTO TIMETABLE VALUES(2, "10:00:00", "11:00:00");""",
"""INSERT INTO TIMETABLE VALUES(3, "11:20:00", "12:20:00");""",
"""INSERT INTO TIMETABLE VALUES(4, "12:25:00", "13:25:00");""",
"""INSERT INTO TIMETABLE VALUES(5, "14:30:00", "15:30:00");"""
]

FILL_SUPPLIER = [
"""INSERT INTO SUPPLIER VALUES(0, "Amazon", "999", "amazon@gmail.com");""",
"""INSERT INTO SUPPLIER VALUES(1, "Ebay", "911", "ebay@gmail.com");""",
"""INSERT INTO SUPPLIER VALUES(2, "AliExpress", "111", "ali@gmail.com");"""
]

FILL_STOCK = [
"""INSERT INTO STOCK VALUES(0, "Sponge (qty)", 10, 299, "https://google.com", 0);""",
"""INSERT INTO STOCK VALUES(1, "Test Tubes (qty)", 5, 1999, "https://google.com", 1);""",
"""INSERT INTO STOCK VALUES(2, "Boiling Tube (qty)", 3, 1599, "https://google.com", 1);""",
"""INSERT INTO STOCK VALUES(3, "HCl (mL)", 1000, 999, "https://google.com", 2);""",
"""INSERT INTO STOCK VALUES(4, "Springs (qty)", 100, 999, "https://google.com", 0);"""
]

FILL_BOOKINGS = [
"""INSERT INTO BOOKINGS VALUES(0, 0, 0, 1, "04-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(1, 1, 1, 2, "04-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(2, 2, 2, 3, "04-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(3, 0, 2, 4, "04-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(4, 1, 0, 5, "04-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(5, 0, 0, 1, "05-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(6, 1, 1, 2, "05-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(7, 2, 2, 3, "05-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(8, 0, 2, 4, "05-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(9, 1, 0, 5, "05-12-2023")""",
#"""INSERT INTO BOOKINGS VALUES(10, 1, 0, 3, "05-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(11, 0, 0, 1, "06-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(12, 1, 1, 2, "06-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(13, 2, 2, 3, "06-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(14, 0, 2, 4, "06-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(15, 1, 0, 5, "06-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(16, 1, 0, 3, "06-12-2023")""",
"""INSERT INTO BOOKINGS VALUES(17, 0, 1, 3, "06-12-2023")"""
]

FILL_BOOKED_STOCK = [
"""INSERT INTO BOOKED_STOCK VALUES(1, 3, 250)""",
"""INSERT INTO BOOKED_STOCK VALUES(2, 0, 1)""",
"""INSERT INTO BOOKED_STOCK VALUES(0, 1, 3)"""
]

TEST_QUERY = """
SELECT USERS.Name, STOCK.Name, BOOKED_STOCK.Amount, BOOKINGS.Time, LABS.Name
FROM BOOKINGS
JOIN BOOKED_STOCK ON BOOKED_STOCK.BookingID=BOOKINGS.BookingID
JOIN STOCK ON STOCK.StockID=BOOKED_STOCK.StockID
JOIN LABS ON BOOKINGS.LabID=LABS.LabID
JOIN USERS ON USERS.UserID=BOOKINGS.UserID
"""