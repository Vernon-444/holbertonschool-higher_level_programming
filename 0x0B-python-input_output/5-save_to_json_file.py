#!/usr/bin/python3
"""Writes obj to text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes obj to text file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
        f.close
