#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    post_req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(post_req) as response:
        email_response = response.read().decode('utf-8')
    print(f"Your email is: {email_response}")
