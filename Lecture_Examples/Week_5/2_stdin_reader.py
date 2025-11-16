#!/usr/bin/env python3
# 2_stdin_reader.py

import sys

for line in sys.stdin:
    # The .strip() method removes leading/trailing whitespace, including the newline
    print(f"Received from the pipe: '{line.strip()}'")
