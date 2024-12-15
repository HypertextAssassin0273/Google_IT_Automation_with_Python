#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())


# NOTE: it capitalizes the first letter of each word, and lowercase the rest in each line of the input.
