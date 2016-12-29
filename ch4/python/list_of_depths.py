#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth (e.g. if you have a tree with depth D, you'll have
D linked lists).
Complexity: O(N)
Usage: list_of_depths <input_size>
'''

# import problem 4.2
import minimal_tree as mt


# functions
def answer(data):

    # binary tree
    tree = BinaryTree(data)

    # traversal
    tree.list_depths()


# classes
class BinaryTree(mt.Tree):
    '''
    Class that inherits from 'Tree' class and implements algorithmic solution
    to the above problem
    '''
    # constructor
    def __init__(self, data):
        mt.Tree.__init__(self, data)

    def list_depths(self):
        '''
        Method to print out list of nodes at each depth
        '''
        # get root of BST
        node_list = [self.root_node]

        # print list of levels
        while len(node_list):

            # reset temp
            temp = []

            # get child nodes
            for node in node_list:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            # copy temp list
            print node_list
            node_list = temp[:]


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
