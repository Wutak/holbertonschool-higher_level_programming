#!/usr/bin/python3
"""safe filter"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name = '%s' "
            "ORDER BY id ASC;".format(state_name,))

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
