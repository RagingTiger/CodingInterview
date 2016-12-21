#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given a sorted array of N integers that has been rotated an unknown number
of times, write code to find an element in the array. You may assume that the
array was originally sorted in increasing order.
Complexity: O(Lg N)
Usage: search_in_rotated_array
'''


def binary_search(array, n):

    # recursive
    index = binary_search(array, n)

    # if not found
    return index if type(index) is int else 'Not Found'


def boundary_search(array, n):

    # look at middle index and index - 1, index + 1
    if array[i] > array[i + 1]:
        return i


def answer(array, n):

    # first determine if rotated
    if array[0] < array[len(array) - 1]:
        # lg N
        return binary_search(array, n)

    # then find boundary index
    boundary = boundary_search(array, n)

    # then choose subarray containing element within range
    if n >= array[0]:
        subarray = array[0:boundary+1]

    elif n < array[0]:
        subarray = array[boundary+1: len(array)]

    else:
        return 'Not Found'

    # finally do binary search
    return binary_search(array, n)


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)
