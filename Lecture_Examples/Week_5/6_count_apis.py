#!/usr/bin/env python3
# 6_count_apis.py: Counts and lists APIs from piped JSON

import sys
import json

# Read the JSON objects one by one (because jq outputs them on separate lines)
api_list = [json.loads(line) for line in sys.stdin]

# Perform the Python-specific logic
count = len(api_list)
print(f"We found {count} Transportation APIs:")

for api in api_list:
    print(f"  - {api['API']} ({api['Auth']})")
