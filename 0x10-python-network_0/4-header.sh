#!/bin/bash
# Send a GET request to the URL, and display body of response
url="$1"
curl -s -H "X-School-User-Id: 98" "$url"
