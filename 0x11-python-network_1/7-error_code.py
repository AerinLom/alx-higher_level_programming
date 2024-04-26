#!/usr/bin/python3
"""
A script that takes in a URL and prints error codes
"""


if __name__ == "__main__":
    import requests
    import sys

    input_url = sys.argv[1]
    error_response = requests.get(input_url)

    if error_response.status_code >= 400:
        print(f"Error code: {error_response.status_code}")
    else:
        print(error_response.text)
