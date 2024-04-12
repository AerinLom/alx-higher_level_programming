#!/usr/bin/python3
"""Lists all cities for each state from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    cursor = database.cursor()
    state = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities INNER JOIN "
                   "states ON states.id=cities.state_id WHERE states.name"
                   " LIKE %s", (state, ))
    results = cursor.fetchall()
    cities = ' '.join(row[0] for row in results)
    print(cities)
    cursor.close()
    database.close()
