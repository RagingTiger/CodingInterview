#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Implement a function to check if a binary tree is balanced. For the purpose
of this question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ more than one.
Complexity: O(N)
Usage: checked_balanced <input_size>
'''


# libraries
import list_of_depths as ld


# functions
def answer(data):

    # build tree
    tree = BalancedTree(data)

    # check if balanced
    print tree.balanced()


# classes
class BalancedTree(ld.BinaryTree):
    '''
    Class to implement binary tree and balance checking method
    '''
    # constructor
    def __init__(self, array):
        ld.BinaryTree.__init__(self, array)

    # balance check
    def balanced(self):
        '''
        Method to kick off recursive traversal to check tree balance
        '''
        # start recursion
        return 'Balanced' if self._check_balance(self.root_node, 0) else \
               'Unbalanced'

    def _check_balance(self, node, count):
        '''
        Private method to recursively check if a tree is balanced
        '''
        if node:
            left = self._check_balance(node.left, count+1)
            right = self._check_balance(node.right, count+1)
            return not (left - right)**2 >> 1
        else:
            return count


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
