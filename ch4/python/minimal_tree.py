#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given a sorted (increasing order) array with unique integer elements, write
an algorithm to create a binary search tree with minimal height.
Complexity: O(N)
Usage: minimal_tree <traversal_order>
'''


# functions
def answer(array, order):

    # get instance of Tree
    tree = Tree(array)

    # traverse
    tree.traverse(order)


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
        node.right = self._recursive_build_tree(array[root+1:length])

        # return
        return node

    def traverse(self, funcname):
        '''
        Private method accepts string of desired traversal method
        '''
        # now execute passed function
        exec 'self._{0}(self.root_node)'.format(funcname)

    def _inorder(self, node):
        '''
        Private method to traverse tree inorder
        '''
        # check if 'None'
        if node:
            # first vist left child
            self._inorder(node.left)

            # then visit parent
            print node.value

            # last visit right child
            self._inorder(node.right)

    def _preorder(self, node):
        '''
        Private method to traverse tree preorder
        '''
        # check if 'None'
        if node:
            # first vist the parent
            print node.value

            # then visit the left child
            self._preorder(node.left)

            # then visit the right child
            self._preorder(node.right)

    def _postorder(self, node):
        '''
        Private method to traverse tree postorder
        '''
        # check if 'None'
        if node:
            # first vist left child
            self._postorder(node.left)

            # then vist right child
            self._postorder(node.right)

            # then visit parent
            print node.value


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

    # for printing and repr()
    def __repr__(self):
        return '{0} {1}: object at {2}'.format(self.__class__.__name__,
                                               self.value, id(self))


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # get args
    args = docopt(__doc__)

    # test data
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # run
    answer(data, args['<traversal_order>'])
