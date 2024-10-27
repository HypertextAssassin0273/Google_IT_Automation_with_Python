#!/usr/bin/env python3

import os, subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

# script break-down:
# 1) import the os and subprocess modules
# 2) create a copy of the current environment variables
# 3) update the PATH environment variable to include the path to our custom application
# 4) finally, run the custom application using the updated environment variables
