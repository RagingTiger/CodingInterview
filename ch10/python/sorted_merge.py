#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    You are given two sorted arrays, A and B, where A has a large enough buffer
    at the end to hold B. Write a method to merge B into A in sorted order.
Usage:
    sorted_merge <A> <B>
    sorted_merge case1
    sorted_merge case2
'''


def answer(a, b):
    print 'under construction'


# executable
if __name__ == '__main__':

    # exectuable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    answer(args['<A>'], args['<B>'])
