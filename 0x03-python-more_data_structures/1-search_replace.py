#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if len(my_list) > 0:
        new = my_list.copy()
        for i in range(0, len(my_list) - 1):
            if new[i] == search:
                new[i] = replace
        return new
    return None