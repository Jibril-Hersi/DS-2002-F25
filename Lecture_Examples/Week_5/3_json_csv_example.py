#!/usr/bin/env python3
# 3_json_csv_example.py

import sys, json, csv

# Read the JSON from the pipe
data = json.loads(sys.stdin.read())

# Create a CSV writer that writes to stdout
writer = csv.DictWriter(sys.stdout, fieldnames=['name', 'age'])

# Write the header row
writer.writeheader()

# Iterate through the JSON data and write to CSV
for person in data['people']:
    writer.writerow(person)
