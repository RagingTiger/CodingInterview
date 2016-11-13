#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Write a program to sort a stack such that the smallest items are on the
top. You can use an additional temporary stack, but you may not copy the
elements into any other data structure (such as an array). The stack supports
the following operations: push, pop, peek, and isEmpty.
Complexity: TODO
Usage:
    sort_stack case1
    sort_stack case2
    sort_stack case3
'''

# libraries
import random


# function
def answer(stack):

    # sort stack
    stack.sort()  # hehehehe

    # return
    return stack

# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # control flow
    if args['case1']:
        stack = random.sample(range(1, 100), random.randint(1, 10))

    elif args['case2']:
        stack = random.sample(range(1, 100), random.randint(1, 100))

    elif args['case3']:
        stack = random.sample(range(1, 1000), random.randint(1, 1000))

    # print answer
    print answer(stack)
