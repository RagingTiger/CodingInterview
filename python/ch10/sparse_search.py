#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given a sorted array of strings that is interspersed with emtpy strings,
write a method to find the location of a given string.
EXAMPLE
Input: ball, {"at", "", "", "", "ball", "", "", "cat", "", "", "dad", "", ""}
Output: 4
Complexity: O(N)
Usage: sparse_search case1
'''


# function
def answer(string, array):

    # check for string
    if string in array:
        for i, s in enumerate(array):
            if s is string:
                return i

    # exit
    return None

# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # control flow
    if args['case1']:
        string = 'bad'
        array = ['abba', '', 'back', 'bad', '', '', '', 'cat', 'dance', 'gray']

    # run
    print answer(string, array)
