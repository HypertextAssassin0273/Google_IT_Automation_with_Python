#!/usr/bin/env bash

line="-------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME:"; uptime; echo $line

echo "FREE:"; free; echo $line

echo "WHO:"; who; echo $line

echo "Finishing at: $(date)"


# SIDE-NOTE: who command will not work for WSL, as it does not have the utmp file.