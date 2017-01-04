#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Implement an algorithm to delete a node in the middle (i.e. any node but
the first and last node, not necessarily the exact middle) of a singly linked
list given only access to that node.
Complexity: O(N)
Usage: TODO
'''

# code from 'return_kth_to_last.py'
import return_kth_to_last as rktl


# classes
class LinkedList(rktl.LinkedList):
    '''
    Class for Linked List with a 'delete_node' method
    '''
    # constructor
    def __init__(self, data):

        # call super class
        rktl.LinkedList.__init__(self, data)

    def delete_node(node):
        '''
        Method for deleting a node
        '''
        while (node.next.next is None):
            node.val = node.next.val
            node.val = node.next.val
            node.next = None


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt
