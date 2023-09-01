#!/usr/bin/python3
"""
Takes URL, sends request,
displays value of X-Request-Id variable in the response header
"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
