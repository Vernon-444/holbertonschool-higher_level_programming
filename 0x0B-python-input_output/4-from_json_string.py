#!/usr/bin/python3
"""Returns an object (python data struct)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """Compile to obj and return"""
    pyth_obj = json.loads(my_str)
    return pyth_obj