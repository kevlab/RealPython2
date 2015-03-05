# SQLite functions

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a dict of sql querres
    sql = {'average': "SELECT avg(population) FROM population",
           'maximum': "SELECT max(population) FROM population",
           'minimum': "SELECT min(population) FROM population",
           'sum': "SELECT sum(population) FROM population",
           'count': "SELECT count(population) FROM population"}

    # run each sql querries
    for key, val in sql.iteritems():

        c.execute(val)

        result = c.fetchone()

        print key + ":", result[0]
