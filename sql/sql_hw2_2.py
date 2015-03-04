import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    print "DATA:\n"

    c.execute("SELECT * FROM inventory WHERE make = 'Ford'")

    data = c.fetchall()

    for _ in data:
        print _[0], _[1], _[2]
