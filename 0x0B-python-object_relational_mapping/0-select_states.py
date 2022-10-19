#!/usr/bin/python3
"""This python script lists all states from the database hbtn_0e_0_usa"""


import MySQLdb


def list_states():
    """This method lists all the states in the table"""
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
