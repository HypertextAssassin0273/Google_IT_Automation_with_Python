#!/usr/bin/env bash

if grep "127\.0\.0\.1" /etc/hosts; then
	echo "Everything ok"
else
	echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi


# NOTE: use 'echo $?' to see the exit status of the last command
