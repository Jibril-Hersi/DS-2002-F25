#!/usr/bin/env python3
# 8_requests_example.py

import requests
import json

try:
    # Make a simple GET request to the API
    response = requests.get('https://api.publicapis.org/entries')

    # Check if the request was successful
    response.raise_for_status()

    # Get the JSON data as a Python dictionary
    data = response.json()
    print(f"Successfully fetched {len(data['entries'])} API entries.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}", file=sys.stderr)
