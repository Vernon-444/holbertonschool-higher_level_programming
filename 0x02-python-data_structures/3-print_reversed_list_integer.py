#!/usr/bin/python3
from re import M


def print_reversed_list_integer(my_list=[]):
    if len(my_list) < 1:
        return
    i = len(my_list) - 1
    while i > -1:
        print("{:d}".format(my_list[i]))
        i -= 1
