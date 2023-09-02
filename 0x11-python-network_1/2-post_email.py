#!/usr/bin/python3
"""
takes URL and email, sends POST request to URL with email as parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = parse.urlencode(value).encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
