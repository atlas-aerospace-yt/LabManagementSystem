"""
A demo to fill the database.
"""

FILL_USERS = [
"""INSERT INTO USERS VALUES(0, "Bob Smith", "b-smith@gmail.com", "&*^GDH^%^^£WdS", 1);""",
"""INSERT INTO USERS VALUES(1, "Adam Baker", "a-baker@gmail.com", "&*^GDH^%^^£WdS", 1);""",
"""INSERT INTO USERS VALUES(2, "Chloe Allan", "c-allan@gmail.com", "&*^GDH^%^^£WdS", 1);""",
"""INSERT INTO USERS VALUES(3, "Sheldon Cooper", "s-cooper@gmail.com", "&*^GDH^%^^£WdS", 2);""",
"""INSERT INTO USERS VALUES(4, "Josh Fruzza", "j-fruzza@gmail.com", "&*^GDH^%^^£WdS", 1);""",
"""INSERT INTO USERS VALUES(5, "Igor Ross", "i-rossh@gmail.com", "&*^GDH^%^^£WdS", 3);"""
]

FILL_LABS = [
"""INSERT INTO LABS VALUES(0, "Physics", "At the end of the science corridor.");""",
"""INSERT INTO LABS VALUES(1, "Chemistry", "The room before Physics.");""",
"""INSERT INTO LABS VALUES(2, "Biology", "Not a science.");""",
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