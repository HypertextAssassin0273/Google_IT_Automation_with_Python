#!/bin/bash

meeting_info=$(zenity --forms\
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' \
    --add-entry 'Title' --add-entry 'Emails' \
    --forms-date-format='%Y-%m-%d' \ # change default date format
    2>/dev/null)

echo $meeting_info # print the output to ensure it's correct

if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "$meeting_info"
fi
