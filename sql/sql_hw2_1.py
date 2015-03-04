import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET quantity = 9 WHERE make = 'Ford'")
    c.execute("UPDATE inventory SET quantity = 8 WHERE make = 'Honda'")

    print "DATA:\n"

    c.execute("SELECT * FROM inventory")

    data = c.fetchall()

    for _ in data:
        print _[0], _[1], _[2]
