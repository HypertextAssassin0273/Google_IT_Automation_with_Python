#!/bin/bash

# DUMMY SCRIPT: for understanding how to reduce cpu usage by un-daemonizing the ffmpeg processes
# ACTUAL WORKING: this script runs ffmpeg in parallel to convert all of thr webm files to mp4 files.

echo "Starting video conversion"
for video in static/*.webm; do
    mp4_video="$(echo $video | sed 's/.webm/.mp4/')"
    # daemonize -c $PWD /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video" # runs in (background as) parallel
    /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video" # runs sequentially
done

# ref: slow-web-server lecture
