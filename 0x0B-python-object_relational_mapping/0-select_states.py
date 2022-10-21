#!/usr/bin/python3
"""Module contains a script that will list all states in a MySQL database"""
import MySQLdb
from sys import argv


def select_states():
    """lists all states from the database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    select_states()
