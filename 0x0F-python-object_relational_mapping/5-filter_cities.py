#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name \
              FROM cities JOIN states ON cities.state_id = states.id \
              WHERE states.name = '{}'".format(sys.argv[4]))
    states = c.fetchall()

    print(", ".join([state[1] for state in states]))
