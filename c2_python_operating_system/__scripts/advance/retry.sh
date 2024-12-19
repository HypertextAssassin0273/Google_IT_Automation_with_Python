#!/bin/bash

n=0
command=$1

while ! $command; do
    if [ $n -ge 5 ]; then
        echo "The command has failed after $n attempts."
        exit 1
    fi
    sleep $n
    ((n+=1))
    echo "Retry #$n"
done


# USAGE: ./retry.sh <command>
# EXAMPLE: ./retry.sh ./random_exit.py
