#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys

# Check if both URL and email are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send a POST request with the email parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Read and display the body of the response (decoded in utf-8)
        body = response.read().decode('utf-8')
        print(body)

except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
