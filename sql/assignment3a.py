import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS randomint")
    c.execute("CREATE TABLE randomint(integers INT)")

    ints = [(random.randint(0, 100),) for _ in range(100)]

    c.executemany("INSERT INTO randomint VALUES(?)", ints)
