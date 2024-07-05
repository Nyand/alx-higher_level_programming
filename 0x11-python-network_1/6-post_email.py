#!/usr/bin/python3
"""This script takes in a URL and an email address, sends a
POST request to the passed URL with the email as a
parameter, and finally displays the body of the response."""
import requests
import sys

# Check if both URL and email are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = {'email': email}

try:
    # Send a POST request with the email parameter
    response = requests.post(url, data=data)
    print(response.text)

except requests.RequestException as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
