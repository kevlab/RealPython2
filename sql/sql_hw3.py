import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date TEXT)")

    some_cars = [('Ford', 'Fiesta', '1999-12-03'),
                 ('Ford', 'Fiesta', '2000-01-30'),
                 ('Ford', 'Fiesta', '2004-02-03'),
                 ('Ford', 'Fiesta', '2010-11-11'),
                 ('Honda', 'Accord', '2001-10-22'),
                 ('Honda', 'Accord', '2009-03-07'),
                 ('Honda', 'Accord', '2008-01-23')]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", some_cars)
