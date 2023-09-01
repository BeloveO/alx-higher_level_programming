#!/bin/bash
# Makes a request to a port, cause response with specified message
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:You got me!"
