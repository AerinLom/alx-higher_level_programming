#!/bin/bash
# Sends a request to a URL, displaying the size of the body of the response
curl -s "$1" | wc -c
