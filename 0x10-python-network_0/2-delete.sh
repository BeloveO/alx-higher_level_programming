#!/bin/bash
# sends DELETE request to first argument url, displays the body response
curl -sX DELETE "$1"
