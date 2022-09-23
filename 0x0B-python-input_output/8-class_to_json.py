#!/usr/bin/python3
"""returns dictionary description with simple
data struct (list, dict, string, int, bool)
for JSON serialization of an object"""

def class_to_json(obj):
    """This function does the work of this module
    """
    return vars(obj)
