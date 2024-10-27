#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

print("Welcome to this time converter")

choice = "y"
while(choice.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print(f"{hours} hr, {minutes} min, {seconds} sec = {to_seconds(hours, minutes, seconds)} secs\n")
    
    choice = input("Do you want to do another conversion? [y to continue] ")
    
print("Goodbye!")
