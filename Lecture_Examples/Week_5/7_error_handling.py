#!/usr/bin/env python3
# 7_error_handling.py

import sys
import json

try:
    data = json.loads(sys.stdin.read())
    print("JSON loaded successfully!")

    # Attempt to access a key that might not exist
    print(f"Name is: {data['name']}")

except json.JSONDecodeError:
    print("Error: Invalid JSON input was received.", file=sys.stderr)
    sys.exit(1)

except KeyError:
    print("Error: The 'name' key was not found.", file=sys.stderr)
    sys.exit(1)
