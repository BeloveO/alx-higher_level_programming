#!/usr/bin/python3
"""
Takes URL, sends request to URL and
displays the body of the response (decoded in utf-8)
"""

from urllib import error, request
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
