""""
This file holds the definitions for the SQl requests that the client
side sends to the server side.
"""

GET_BOOKINGS_INFO = """
SELECT USERS.Forename, USERS.Surname, LABS.Name, BOOKINGS.Date, TIMETABLE.StartTime, TIMETABLE.EndTime
FROM BOOKINGS
JOIN TIMETABLE ON BOOKINGS.TimeID = TIMETABLE.TimeID
JOIN USERS ON BOOKINGS.UserID = USERS.UserID
JOIN LABS ON BOOKINGS.LabID = LABS.LabID
"""

GET_LABS = "SELECT LabID, Name FROM LABS"

GET_STOCK_AND_SUPPLIER = """SELECT STOCK.StockID, STOCK.Name, STOCK.Amount, STOCK.Price, STOCK.Website,
SUPPLIER.Name, SUPPLIER.Email, SUPPLIER.Phone
FROM STOCK JOIN SUPPLIER ON STOCK.SupplierID=SUPPLIER.SupplierID"""

STOCK_AND_SUPPLIER_VARS = [
"STOCK.StockID",
"STOCK.Name",
"STOCK.Amount",
"STOCK.Price",
"STOCK.Website",
"SUPPLIER.Name",
"SUPPLIER.Email",
"SUPPLIER.Phone"
]

