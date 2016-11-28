#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Write an algorithm to print all ways of arranging eight queens on an 8 x 8
chess board so that none of them share the same row, column, or diagonal. In
this case, "diagonal" means all diagonals, not just the two that bisect the
board.
Complexity: TODO
Usage: TODO
'''


# functions
def answer(x):

    # gen matrix
    chess_board = [[0 for x in range(8)] for x in range(8)]
