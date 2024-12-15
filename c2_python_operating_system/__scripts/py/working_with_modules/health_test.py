#!/usr/bin/env python3

import shutil, psutil
from __modules.network import *

def check_disk_usage(disk, threshold=20):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > threshold

def check_cpu_usage(threshold=75):
    usage = psutil.cpu_percent(1)
    return usage < threshold

if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything is OK!")
else:
    print("Network Checks Failed!")


# NOTE: one good example of 'when to use' an 'automatation script' can be,
# "to detect dangerously high CPU usage levels across a network
# and scale back the CPU clock speeds of those devices,
# or shut them down to prevent overheating."
