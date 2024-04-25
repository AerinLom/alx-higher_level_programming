#!/bin/bash
# Send a GET request to the URL, and display body of response
url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"
curl -s -X POST -d "email=$email" -d "subject=$subject" "$url"
