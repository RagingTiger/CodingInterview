#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given a sorted (increasing order) array with unique integer elements, write
an algorithm to create a binary search tree with minimal height.
Complexity: O(N)
Usage: minimal_tree
'''


# functions
def answer(array):

    tree = Tree(array)


# classes
class Tree(object):
    '''
    Class to implement a binary tree
    '''
    # constructor
    def __init__(self, array):

        self.root_node = _recursive_tree_build(array)

    # internal method
    def _recursive_build_tree(self, array):

        # get length
        length = len(array)

        # check
        if not length:
            return None

        # calculate root
        root = length / 2

        # create Node
        node = Node(array[root])

        # get left and right node
        node.left = self._recursive_build_tree(array[0:root])
        node.right = self._recursive_build_tree(array[root:length-1])

        # return
        return node

    # internal method
    def _traverse(self, node):
        '''
        Private method to be used in traversal
        '''
        pass

    def inorder(self):
        '''
        Method to traverse tree inorder
        '''
        pass

    def preorder(self):
        '''
        Method to traverse tree preorder
        '''
        pass

    def postorder(self):
        '''
        Method to traverse tree postorder
        '''
        pass


class Node(object):
    '''
    Class to implement node for binary tree
    '''
    # constructor
    def __init__(self, value):
        # store value
        self.value = value

        # store left node
        self.left = None

        # store right node
        self.right = None


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # get args
    args = docopt(__doc__)

    # test data
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # run
    answer(data)
