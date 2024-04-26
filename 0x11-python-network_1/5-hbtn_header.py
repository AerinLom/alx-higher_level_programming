#!/usr/bin/python3
"""
A script that requests a URL and displays value of variable X-Request-Id
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
