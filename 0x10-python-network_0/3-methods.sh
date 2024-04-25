#!/bin/bash
# Displays all methods the server will accept
curl -s -X OPTIONS -i "$1" | grep -i '^Allow:' | cut -d " " -f 2-
