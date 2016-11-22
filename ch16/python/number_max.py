#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Write a method that finds the maximum of two numbers. You should not use
if-else or any comparison operator.
Complexity: TODO
Usage: number_max <x> <y>
'''

# libraries
import math


# functions
def answer(x, y):

    # return
    return (math.fabs(x - y) + (x + y))/2


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # return
    print answer(int(args['<x>']), int(args['<y>']))
