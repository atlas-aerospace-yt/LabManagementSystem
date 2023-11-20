""""
This file holds the definitions for the SQl requests that the client
side sends to the server side.
"""

GET_BOOKINGS_INFO = """
SELECT USERS.Forename, USERS.Surname, LABS.Name, Date TIMETABLE.StartTime FROM BOOKINGS
JOIN TIMETABLE ON TIMETABLE.TimeID = BOOKINGS.TimeID
JOIN USERS ON USERS.UserID = BOOKINGS.UserID
JOIN LABS ON LABS.LabID = BOOKINGS.LabID;
"""