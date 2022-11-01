#!/usr/bin/python3

"""Fetches status of Holberton Intranet"""

if __name__ == "__main__":
    from urllib import request

    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as page:
        page = page.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode('utf8')))
