#!/usr/bin/env python3
# env_vars.py

import os

# Get the value of the 'API_KEY' environment variable
api_key = os.getenv('API_KEY')

print(f"My API Key is: {api_key}")
