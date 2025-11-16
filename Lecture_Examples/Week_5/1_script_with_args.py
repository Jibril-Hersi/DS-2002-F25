#!/usr/bin/env python3
# 1_script_with_args.py

import sys

print(f"The script's name is: {sys.argv[0]}")

if len(sys.argv) > 1:
    print(f"The first argument is: {sys.argv[1]}")
