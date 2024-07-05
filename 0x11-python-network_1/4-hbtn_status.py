#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)

    # Displaying the body of the response with tabulation before each line
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

except requests.RequestException as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
