#!/usr/bin/env python3

import sys # for accessing command line arguments

def character_frequency(filename):
    '''Counts the frequency of each character in the given file.'''
    with open(filename) as f:
        frequency = {} # dictionary (to hold the frequency of each character)
        for line in f:
            for char in line:
                frequency[char] = frequency.get(char, 0) + 1 # error handling
        return frequency

# Test the function
if __name__ == '__main__': # execute only if it's run as a standalone program
    try:
        filename = sys.argv[1]
        print(character_frequency(filename))

    except IndexError: # if no command line argument is provided
        print("Usage: char_freq.py <filename>")

    except OSError: # if file not found
        print(f"Error: {filename} not found!")


# side-note: in order to use 'Exception' class, it needs to be derived from base class (as pre-req)
