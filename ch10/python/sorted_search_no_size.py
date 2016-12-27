#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    You are given an array-like data structure Listy which lacks a size method.
It does, however, have an elementAt(i) method that returns the element at index
i in O(1) time. If i is beyond the bounds of the data structure, it returns -1.
(For this reason, this data structure only support positive int). Given a Listy
which contains sorted, positive integers, find the index at which an element x
occurs. If x occurs multiple times, you may return any index.

Example:
1, 2, 2, 3, 4, 5, 5, 8, 8, 9, 9, 9   x = 8
'''


# First most basic answer: O(N)
def answer(x, array):
    i = 0
    while True:
        if array.elementAt(i) == x:
            return i
        elif array.elementAt(i) < x:
            i += 1
        else:
            return False


# Now a more advanced answer: O(LgN) ?
    # Questions:
        # Implement a size method?
        # Test if “IN BOUND” or “OUT of BOUND”
        # O(LgN + LgN) = O(2LgN) = O(LgN)
