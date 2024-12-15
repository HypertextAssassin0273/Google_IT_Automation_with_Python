#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", "")) # environ -> dictionary
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# NOTE: we can avoid 'KeyError' by using 'dictionary.get(key, default)' method


# --------------------------------------------------------------------- #
# Set the environment variable (for current shell):
# export FRUIT=Pineapple

# NOTE: no spaces around '=' sign when setting the environment variable
# --------------------------------------------------------------------- #
