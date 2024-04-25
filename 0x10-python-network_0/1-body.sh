#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
url="$1"
curl -s -L "$url"
