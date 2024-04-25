#!/bin/bash
# Send DELETE request to URL passed as first argument and display body of the response
curl -s -X DELETE "$1"
