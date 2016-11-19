#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given an input file with four billion non-negative integers, provide an
algorithm to generate an integer that is not contained in the file. Assume you
have 1GB of memory available for this task.
FOLLOW UP
What if you have only 10MB of memory? Assume that all values are distinct and
we now have no more than one billion non-negative integers.
References: Programming Pearls: chapter 2 "Aha! Algorithms"
Complexity: O(N)
Usage:
    missing_int -m <input_file>
    missing_int test
'''

# libraries
import random


# functions
def answer(integers):
    '''
    Function to find a missing integer in a list of 0 < N <= 2^32 - 1.
    '''
    # sort ints
    integers.sort

    # check for missing int
    for i, e in enumerate(integers):

        if i is not e:
            return i

    # else none
    return None


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # control flow
    if args['test']:
        integers = random.sample(range(0, 100), random.randint(0, 100))

    else:
        integers = args['<input_file>']

    # run
    print answer(integers)
