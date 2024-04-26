#!/usr/bin/python3
"""
Accepts GitHub credentials then displays an ID
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    github_api_url = "https://api.github.com"
    git_user_endpoint = f"{github_api_url}/user"
    authentication = (username, password)

    git_response = requests.get(git_user_endpoint, auth=authentication)
    git_user_data = git_response.json()
    git_user_id = git_user_data.get('id')
    print(git_user_id)
