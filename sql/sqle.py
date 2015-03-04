# SELECT statement

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # for loop to iterate through db
    for row in c.execute("SELECT firstname, lastname FROM employees"):
        print row
