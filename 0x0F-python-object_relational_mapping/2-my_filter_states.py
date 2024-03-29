#!/usr/bin/python3
"""
Lists all the states from the required database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
    id ASC".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
