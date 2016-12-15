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

    # get instance of Tree
    tree = Tree(array)

    # traverse
    tree.traverse('inorder')


# classes
class Tree(object):
    '''
    Class to implement a binary tree
    '''
    # constructor
    def __init__(self, array):

        self.root_node = self._recursive_build_tree(array)

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

    def traverse(self, funcname):
        '''
        Private method to be used in traversal. Accepts string of traversal
        method desired.
        '''
        # now execute passed function
        exec 'self._{0}(self.root_node)'.format(funcname)

    def _inorder(self, node):
        '''
        Private method to traverse tree inorder
        '''
        # check if 'None'
        if node:
            # first vist left subtree
            self._inorder(node.left)

            # then visit root
            print node.value

            # last visit right subtree
            self._inorder(node.right)

    def _preorder(self):
        '''
        Private method to traverse tree preorder
        '''
        pass

    def _postorder(self):
        '''
        Private method to traverse tree postorder
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
