#!/bin/bash
# Bash script to take URL, send and displays size of body of response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
