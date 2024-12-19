#!/bin/bash

file=${1:-../../__assets/haiku.txt}
if [ ! -f $file ]; then
    echo "File '$file' not found!"
    exit 1
fi

text=$(cat $file)
for i in $text; do
    B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`
    echo -n "${B}${i:1} "
done

echo -e "\n"


# USAGE: ./capitalize_words.sh <filepath>
# NOTE: logic is too complex & not readable in bash, better to use python for this
