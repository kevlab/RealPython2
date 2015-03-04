# Create a SQlite3 db and table

import sqlite3

# create a new db if it doesn't exist yet
conn = sqlite3.connect("new.db")

# create cursor to execute sql commands
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE population
                  (city TEXT, state TEXT, population INT)
               """)

# close connection
conn.close()
