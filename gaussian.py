#!/usr/bin/env python

import sys
from itertools import islice

# Search the inputted file for a specific phrase, then print the next "x"
# number of lines
def search_file_and_print_lines(inputted_file, search_phrase, next_lines):
    with open(inputted_file, 'r') as f:
        for line in f:
            if search_phrase in line:
                print line,
                print(''.join(islice(f, next_lines)))

def main(inputted_file):
    search_file_and_print_lines(inputted_file, "Item", 5)

if __name__ == "__main__":
    if len(sys.argv[1:]) > 1:
        print "Too Many Arguments!"
        exit(-1)

    inputted_file = sys.argv[1:][0]
    main(inputted_file)
