#!/usr/bin/python3
"""filter cities"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_id = sys.argv[4]
    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.name,
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;""", (state_name,))

    result = cursor.fetchall()
    cities_names = ", ".join(row[0] for row in result)
    print(cities_names)
    cursor.close()
    db.close()
