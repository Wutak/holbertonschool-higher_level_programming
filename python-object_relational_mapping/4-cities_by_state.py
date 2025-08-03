#!/usr/bin/python3
"""cities by state"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id,
    cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;""")

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
