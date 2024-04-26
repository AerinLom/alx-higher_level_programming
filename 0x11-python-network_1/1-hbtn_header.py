#!/usr/bin/python3
"""
A script that takes input url and displays the value of X-Request-Id variable
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers["X-Request-Id"])
