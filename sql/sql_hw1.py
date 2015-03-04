# Create a SQlite3 db and table

import sqlite3

# create a new db if it doesn't exist yet
conn = sqlite3.connect("cars.db")

# create cursor to execute sql commands
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE inventory
                  (make TEXT, model TEXT, quantity INT)
               """)

# close connection
conn.close()
