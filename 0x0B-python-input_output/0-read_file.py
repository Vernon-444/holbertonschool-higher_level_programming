#!/usr/bin/python3
"""Reads content of file and prints it to stdout"""


def read_file(filename=""):
    """Reads content of file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        t = f.read()
        print(t, end="")
