# INSERT command

import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
    # insert data
    cursor.execute(
        "INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    cursor.execute(
        "INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

    # commit
    conn.commit()
except sqlite3.OperationalError:
    print "OOps! I goofed."

conn.close()
