#!/usr/bin/env python3

import os, sys

if len(sys.argv) == 1:
    print("Error: you must provide a filename")
    sys.exit(1)

filename = sys.argv[1]

if os.path.exists(filename):
    print(f"Error: the file '{filename}' already exists!")
    sys.exit(1)

with open(filename, "w") as file:
    file.write("New file created\n")


# SIDE-NOTE: to see the exit code of the last command in shell, use 'echo $?'

# USAGE: ./create_file.py <filename>
