import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("SELECT count(order_date) FROM orders")
    result = c.fetchone()
    print result[0]
