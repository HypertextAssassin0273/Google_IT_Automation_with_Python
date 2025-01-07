#!/bin/bash

# script to change the priority of all (running) ffmpeg processes

for pid in $(pidof ffmpeg); do
    renice -n 19 -p $pid
done

# ref: slow-web-server lecture
