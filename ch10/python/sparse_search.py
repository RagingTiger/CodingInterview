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
Complexity: O(S*LgN)
Usage: sparse_search case1
'''

# NOTES:
# array is sorted (assumed in order from least to greatest)
# this is a “search” problem
# we are returning the given index of the located string or ‘not found’ if not
# found null strings are there to “disrupt” binary search (this implies binary
# search
# is the solution what a surprise !!!!! :) )
# get array.length() / 2
# initial problem is finding a “context string” to know which half to search
# O(lgN) + O(lgN)
#
# WALKTHROUGH:
# # step 1
# {‘at’, ‘’, ‘’, ‘’, ‘ball’, ‘’, ‘’, ‘car’, ‘’, ‘’, ‘dad’, ‘’, ‘’}
#
# array.length()/2 = 6
# array[6] = ‘’
#
# # step 2: recurse binary_search
# binary_search(array[0:6+1], word)
# binary_search(array[6+1:array.length+1], word)


# most basic solution: O(N)
def answer(array, word):

    for i, w in enumerate(array):
        if w == word:
            return i

return 'not found'


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # control flow
    if args['case1']:
        word = 'bad'
        array = ['abba', '', 'back', 'bad', '', '', '', 'cat', 'dance', 'gray']

    # run
    print answer(array, word)
