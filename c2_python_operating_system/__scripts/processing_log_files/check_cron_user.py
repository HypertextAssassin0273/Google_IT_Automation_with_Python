#!/usr/bin/env python3

import sys, re

logfile = sys.argv[1]
with open(logfile) as file:
    pattern = r"CRON.+USER \((.+)\)$"
    for line in file:
        result = re.search(pattern, line)
        if result is not None:
            print(result[1])

# usage: ./check_cron_user.py ../../__assets/syslog
