#!/bin/bash
# Take in a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" |GREP "Allow:" | -d " " -f 2-
