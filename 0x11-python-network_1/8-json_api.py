#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        p = {'q': q}
        url = "http://0.0.0.0:5000/search_user"
        req = requests.post(url, p)

        if {'id', 'name'} <= req.keys():
            id = req.get('id')
            name = req.get('name')
            print('[{id}] {name}'.format(id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
