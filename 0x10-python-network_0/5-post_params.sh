#!/bin/bash
# Takes in a URL, sends a POST request and display response body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
