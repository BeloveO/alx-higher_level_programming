#!/usr/bin/python3
"""
List commits made by rails from recent to oldest
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com"
    uri = '{0}/repos/{1}/{2}/commits'.format(url, sys.argv[2], sys.argv[1])
    req = requests.get(uri).json()
    for i in req[:10]:
        print(i['sha'] + ':', i['commit']['author']['name'])
