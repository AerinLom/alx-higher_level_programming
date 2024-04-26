#!/usr/bin/python3
"""
A script that takes a URL, requests the URL and displays value of variable X-Request-Id
"""


if __name__ == "__main__":
    from requests import get
    import sys

    url = sys.argv[1]
    response = get(url)
    print(response.headers.get('X-Request-Id'))
