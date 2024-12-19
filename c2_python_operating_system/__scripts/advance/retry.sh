#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;


# USAGE: ./retry.sh <command>
# EXAMPLE: ./retry.sh ./random_exit.py
