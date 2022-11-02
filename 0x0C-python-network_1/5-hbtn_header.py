#!/usr/bin/python3
"""
This script displays the X-Request-ID from a passed in URL
"""
import requests
import sys


if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get('X-Request-Id'))
