#!/bin/bash

for logfile in *log; do # process all files with log extension in current directory
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done


# NOTE: you can do this with actual system log files by replacing '*log' with '/var/log/*log'
