#!/bin/bash

# script to make ffmpeg processes resume as sequential processes

killall -STOP ffmpeg # pause all ffmpeg processes

for pid in $(pidof ffmpeg); do # resume ffmpeg processes sequentially
    while kill -CONT $pid; do # wait for next process until current one is done
        sleep 1
    done
done

# ref: slow-web-server lecture
