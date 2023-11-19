"""
A demo to fill the database.

https://learnsql.com/blog/how-to-join-3-tables-or-more-in-sql/
"""

FILL_USERS = [
"""INSERT INTO USERS VALUES(0, "Bob Smith", "b-smith@gmail.com", "827ccb0eea8a706c4c34a16891f84e7b", 1);""",
"""INSERT INTO USERS VALUES(1, "Adam Baker", "a-baker@gmail.com", "827ccb0eea8a706c4c34a16891f84e7b", 1);""",
"""INSERT INTO USERS VALUES(2, "Chloe Allan", "c-allan@gmail.com", "827ccb0eea8a706c4c34a16891f84e7b", 1);""",
"""INSERT INTO USERS VALUES(3, "Sheldon Cooper", "s-cooper@gmail.com", "827ccb0eea8a706c4c34a16891f84e7b", 2);""",
"""INSERT INTO USERS VALUES(4, "Josh Fruzza", "j-fruzza@gmail.com", "827ccb0eea8a706c4c34a16891f84e7b", 1);""",
"""INSERT INTO USERS VALUES(5, "Igor Ross", "i-rossh@gmail.com", "827ccb0eea8a706c4c34a16891f84e7b", 3);"""
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
"""INSERT INTO BOOKINGS VALUES(0, 3, 0, 1, "09-11-2023")""",
"""INSERT INTO BOOKINGS VALUES(1, 0, 1, 1, "09-11-2023")""",
"""INSERT INTO BOOKINGS VALUES(2, 5, 2, 2, "09-11-2023")"""
]

FILL_BOOKED_STOCK = [
"""INSERT INTO BOOKED_STOCK VALUES(1, 3, 250)""",
"""INSERT INTO BOOKED_STOCK VALUES(2, 0, 1)""",
"""INSERT INTO BOOKED_STOCK VALUES(0, 1, 3)""",
"""INSERT INTO BOOKED_STOCK VALUES(0, 4, 5)"""
]

TEST_QUERY = """
SELECT USERS.Name, STOCK.Name, BOOKED_STOCK.Amount, BOOKINGS.Time, LABS.Name
FROM BOOKINGS
JOIN BOOKED_STOCK ON BOOKED_STOCK.BookingID=BOOKINGS.BookingID
JOIN STOCK ON STOCK.StockID=BOOKED_STOCK.StockID
JOIN LABS ON BOOKINGS.LabID=LABS.LabID
JOIN USERS ON USERS.UserID=BOOKINGS.UserID
"""