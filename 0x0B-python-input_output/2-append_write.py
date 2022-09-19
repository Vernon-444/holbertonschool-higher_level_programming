#!/usr/bin/python3
"""Appends string at the end of .txt
Returns the number of chars added"""


def append_write(filename="", text=""):
    """Append text to filename and return number of chars added"""

    with open(filename, "a", encoding="utf-8") as f:
        f.write("{}".format(text))
        f.close
    return (len(text))
