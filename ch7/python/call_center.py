#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Imagine you have a call center with three levels of employees: respondent,
manager, and director. An incoming telephone call must be first allocated to a
respondent who is free. If the respondent can't handle the call, he or she must
escalate, the call to a manager. If the manager is not free or not able to
handle it, then the call should be escalated to a director. Design the classes
and data structures for this problem. Implement a method dispatchCall() which
assigns a call to the first available employee.
Complexity: TODO
Usage: TODO
'''

# libraries
import random


# classes
class CallCenter(object):
    pass


class Respondent(object):
    pass


class Manager(object):
    pass


class Director(object):
    pass


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)
