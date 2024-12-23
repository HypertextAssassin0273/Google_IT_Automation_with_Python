#!/usr/bin/env python3

import os, sys, shutil

def disk_full():
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage("/")
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < 20 or gigabytes_free < 2:
        return True
    return False

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

if __name__ == "__main__":
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if disk_full():
        print("Disk Full.")
    print("Everything ok.")
    sys.exit(0)
