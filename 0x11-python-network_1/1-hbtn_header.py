#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response"""
import urllib.request
import sys

# Check if a URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Retrieve and display the value of the X-Request-Id header
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
