#!/usr/bin/python3
"""
A script that takes input url and displays the value of X-Request-Id variable
"""
import urllib.request
import sys


url_dest = sys.argv[1]
with urllib.request.urlopen(url_dest) as response:
    print(response.headers["X-Request-Id"])
