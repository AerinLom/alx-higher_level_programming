#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status using requests
"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
