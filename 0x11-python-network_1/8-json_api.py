#!/usr/bin/python3
"""
sends POST request to http://0.0.0.0:5000/search_user with letter parameter.
"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        input_letter = sys.argv[1]
    else:
        input_letter = ""

    input_url = "http://0.0.0.0:5000/search_user"
    data = {'q': input_letter}
    letter_response = requests.post(input_url, data=data)

    try:
        json_response = letter_response.json()
        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
