#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Design and implement a text-based Minesweeper game. Minesweeper is the
classic single-player computer game where an N x N grid has B mines (or bombs)
hidden across the grid. The remaining cells are either blank or have a number
behind them. The numbers reflect the number of bombs in the surrounding eight
cells. The user then uncovers a cell. If it is a bomb, the player loses. If it
is a number, the number is exposed. If it is a blank cell, this cell and all
adjacent blank cells (up to and including the surrounding numeric cells) are
exposed. The player wins when all non-bomb cells are exposed. The player can
also flag certain places a potential bombs. This doesn't affect game play,
other than block the user from accidentally clicking a cell that is thought to
have a bomb.
Complexity: TODO
Usage: TODO
'''

# libraries
import random


# classes
class MineSweeper(object):
    '''
    Class to implement text version of classic mine sweeper game.
    '''
    # constructor
    def __init__(self, N):

        # generate random cells in range 0 to N^2
        pass

    def run(self):
        '''
        Function to run actual game.
        '''
        pass

    def uncover(self):
        '''
        Function to uncover all 'blank' blocks.
        '''
        pass

    def print_matrix(self):
        '''
        Function to print out current matrix.
        '''
        pass


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)
