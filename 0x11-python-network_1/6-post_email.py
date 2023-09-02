#!/usr/bin/python3
"""
takes URL and email address, sends POST request to URL with the email
as parameter, and finally displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], value)
    print(req.text)
