#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
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
    cursor.execute("SELECT id, name FROM states where name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    database.close()
