#!/usr/bin/env bash

if test -n "$PATH"; then echo "Your path is not empty"; fi

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi


# NOTE: '[]' is an alias for 'test' command & '-n' is a test for non-empty string
