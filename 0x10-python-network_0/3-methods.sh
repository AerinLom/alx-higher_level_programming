#!/bin/bash
# Displays all methods the server will accept
url="$1"
curl -s -X OPTIONS -i "$url" | grep -i '^Allow:' | cut -d " " -f 2-
