import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT
                 orders.make, orders.model, inventory.quantity, orders.order_date
                 FROM orders, inventory
                 WHERE orders.make = inventory.make
                 ORDER BY orders.order_date ASC""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print str(r[2]), r[3]
