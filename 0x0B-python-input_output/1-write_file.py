#!/usr/bin/python3
"""Writes a string to text file (UTF8) and returns num of chars written"""


def write_file(filename="", text=""):
    with open(filename, "w") as f:
        f.write("{}".format(text))
        f.close
    return (len(text))
