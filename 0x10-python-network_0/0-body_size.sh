#!/bin/bash
# Sends a request to a URL, displaying the size of the body of the response
url="$1"
curl -s "$url" | wc -c
