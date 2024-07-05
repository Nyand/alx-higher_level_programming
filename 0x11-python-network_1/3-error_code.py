#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.error
import sys

# Check if a URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Read and display the body of the response (decoded in utf-8)
        body = response.read().decode('utf-8')
        print(body)

except urllib.error.HTTPError as e:
    # Handle HTTPError exceptions and print the HTTP status code
    print(f"Error code: {e.code}")
except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
