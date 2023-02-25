#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    datab = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = datab.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall()]
