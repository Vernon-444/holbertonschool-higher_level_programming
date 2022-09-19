#!/usr/bin/python3
"""Creates an objest from JSON file"""
import json


def load_from_json_file(filename):
    """Get text from json and convert to pyth obj"""
    with open(filename, 'r') as f:
        return(json.load(f))
