#!/usr/bin/python3
"""
A script that takes input url and displays the value of X-Request-Id variable
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers["X-Request-Id"])
