#!/usr/bin/python3
"""
A script that takes in a URL and prints error codes
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
