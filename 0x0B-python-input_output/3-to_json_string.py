#!/usr/bin/python3
"""Returns JSON representaiton of an object (string)"""
import json


def to_json_string(my_obj):
    """Returns JSON rep of the provided obj"""

    jstr = json.dumps(my_obj)
    return (jstr)
