#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Implement a function to check if a binary tree is a binary search tree.
Complexity: TODO
Usage: TODO
'''


# libraries
import check_balanced as cb


# functions
def answer(data):
    pass


# classes
class BST(cb.BalancedTree):
    '''
    Class to implement binary tree and methods to confirm BST
    '''
    # constructor
    def __init__(self, data):
        cb.BalancedTree(data)

    def isBST(self):
        '''
        Method to start recursive traversal to determine if tree is BST
        '''
        return self._is_bst(self.root_node)

    def _is_bst(self, node):
        '''
        Private method for recursive traversal of tree
        '''
        # simplest way is to check immediate nodes
        if node:
            if node.left.val <= node.val <= node.right.val:
                left = self._is_bst(node.left)
                right = self._is_bst(node.right)
                return left and right
            else:
                return false


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # test data
    data = [x for x in range(1, int(args['<input_size>'])+1)]

    # run
    answer(data)
