import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    somecars = [('Ford', 'Fiesta', 3),
                ('Honda', 'Accord', 2)]

    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', somecars)
