import sqlite3
import sys

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    sql = {'AVG': "SELECT avg(integers) FROM randomint",
           'MAX': "SELECT max(integers) FROM randomint",
           'MIN': "SELECT min(integers) FROM randomint",
           'SUM': "SELECT sum(integers) FROM randomint"}
    while True:
        print "Would you like to perform an operation (AVG, MAX, MIN, SUM) or quit?"
        answer = raw_input('(AVG, MAX, MIN, SUM, Quit)> ')
        if answer.lower().startswith('q'):
            sys.exit()
        else:
            try:
                c.execute(sql[answer])
                result = c.fetchone()
                print answer + ":", result[0]
            except KeyError:
                print 'Wrong Command'
