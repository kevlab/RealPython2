# INSERT command

import sqlite3

# create connection object
conn = sqlite3.connect("new.db")

cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# commit
conn.commit()

conn.close()
