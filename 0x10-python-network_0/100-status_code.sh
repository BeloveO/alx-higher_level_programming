#!/bin/bash
# Send request URL passed, and displays only the response status code
curl -so /dev/null -w "%{http_code}" "$1"
