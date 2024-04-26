#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request
"""


if __name__ == "__main__":
    from requests import post
    import sys

    input_url = sys.argv[1]
    input_email = sys.argv[2]
    email_response = post(input_url, {'email': input_email})
    print(email_response.text)
