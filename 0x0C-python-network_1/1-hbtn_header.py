#!/usr/bin/python3
""" Displays the X-Request-ID from
a passed in URL"""


if __name__ == "__main__":
    from urllib import request
    import sys

    req = request.Request(sys.argv[1])
    with request.urlopen(req) as page:
        print(page.info()['X-Request-Id'])
