#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given two (singly) linked lists, determine if the two lists intersect.
    Return the intersecting node. Note that the intersection is defined, based
    on reference, not value. That is, if the kth node of the first linked list
    is the exact same node (by reference) as the jth node of the second linked
    list, then they are intersecting.
Complexity: TODO
Usage:
    intersection case1
    intersection case2
    intersection case3
    intersection -m <N> <M>
'''

# libraries
import random


# functions
def answer(one, two):
    '''
    Function to determine if intersection of two lists exits.
    '''
    # sort in place
    one.sort()
    two.sort()

    # functions
    def recur_search(ls1, ls2, k, j):
        '''
        Function to find intersection of sorted lists.
        '''
        if len(ls2) == j:
            return False
        for i in range(k, len(ls1)):
            if ls2[j] < ls1[i]:
                return recur_search(ls1, ls2, i, j+1)
            elif ls2[j] == ls1[i]:
                return True
        return False

    # start recursion
    return recur_search(one, two, 0, 0)


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # cases
    if args['case1']:
        one = random.sample(range(1, 100), random.randint(1, 10))
        two = random.sample(range(1, 100), random.randint(1, 10))

    elif args['case2']:
        one = random.sample(range(1, 100), random.randint(1, 100))
        two = random.sample(range(1, 100), random.randint(1, 100))

    elif args['case3']:
        one = random.sample(range(1, 1000), random.randint(1, 1000))
        two = random.sample(range(1, 1000), random.randint(1, 1000))

    # print i/o
    print 'list1 - len{1}: {0}'.format(one, len(one))
    print 'list2 - len{1}: {0}'.format(two, len(two))
    print answer(one, two)
