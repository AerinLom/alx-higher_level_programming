#!/usr/bin/python3
"""
A script that takes a URL, requests the URL and displays value of variable X-Request-Id
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    header_id = response.headers['X-Request-Id']
    print(header_id)
