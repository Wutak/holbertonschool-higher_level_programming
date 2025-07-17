#!/usr/bin/python3
"""listing all states"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys,argv[4]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name, port=3306)

    cursor = db.cursor
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(state_name)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
