#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Implement an algorithm to find the kth to last element of a singly linked
list.
Complexity: TODO
Usage: O(N)
'''


# functions
def answer(node, k):
    '''
    Function to traverse singly linked list
    '''


# classes
class LinkedList(object):
    '''
    Class to implement a linked list data structure.
    '''
    # constructor
    def __init__(self, data):
        self.length = len(data)

    def find_kth(self, k):
        '''
        Method to find the kth node
        '''
        # check k
        if k > self.length:
            raise IndexError

        # traverse til k
        temp = self.node
        count = 0
        while (count != k):
            count += 1
            temp = temp.next

        # now traverse to end
        nodek = self.node
        while(temp.next is not None):
            nodek = nodek.next
            temp = temp.next

        # return
        return nodek


class Node(object):
    '''
    Class to implement node for linked list
    '''
    # constructor
    def __init__(self, value):
        # store value
        self.value = value

        # store next node
        self.next = None

    # for printing and repr()
    def __repr__(self):
        return '{0} {1}: object at {2}'.format(self.__class__.__name__,
                                               self.value, id(self))
