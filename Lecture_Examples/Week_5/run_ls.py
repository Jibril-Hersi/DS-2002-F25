#!/usr/bin/env python3
# run_ls.py: Calls the `ls -l` command

import subprocess

# subprocess.run() takes a list of strings
# The first item is the command, the rest are the arguments
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

print("The output of 'ls -l':")
print(result.stdout)
