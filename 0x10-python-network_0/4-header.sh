#!/bin/bash
# Takes in a URL as an argument, sends a GET request, displays response body
curl -s "$1" -H "X-School-User-Id: 98"
