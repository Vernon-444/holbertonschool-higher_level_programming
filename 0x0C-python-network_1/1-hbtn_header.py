#!/usr/bin/python3
""" Displays the X-Request-ID from
a passed in URL"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        info = response.info()
        print(info.get('X-Request-Id'))
