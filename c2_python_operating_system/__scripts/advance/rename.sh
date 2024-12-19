#!/bin/bash

src_ext="${1:-.HTM}" # set source file extension to 1st provided argument or default to .HTM
dest_ext="${2:-.html}" # set desired file extension to 2nd provided argument or default to .html

for file in *"$src_ext"; do # loop through 'all' files in current directory with source extension
    name=$(basename "$file" "$src_ext") # extract file name without extension
    # mv "$file" "$name$dest_ext" # rename file to desired extension
    echo mv "$file" "$name$dest_ext" # for debugging & testing
done


# USAGE: ./rename.sh <source_extension> <destination_extension>
# PRO-TIP: use echo in front of any command & it will only print the command instead of executing it. useful for seeing the complete command before running it.
