#!/bin/bash
# Send DELETE request to URL passed as first argument and display body of the response
url="$1"
curl -s -X DELETE "$url"
