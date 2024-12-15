#!/usr/bin/env python3

import sys, re

usernames = {}
logfile = sys.argv[1]

with open(logfile) as file:
    pattern = r"CRON.+USER \((.+)\)$" # find only CRON users & capture their names from the log
    for line in file:
        result = re.search(pattern, line)
        if result is not None:
            name = result[1]
            usernames[name] = usernames.get(name, 0) + 1 # count the number of times user appears in log

print(usernames)


# USAGE: ./check_cron_user.py ../../../__assets/syslog
