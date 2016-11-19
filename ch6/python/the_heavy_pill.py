#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but on has
pills of 1.1 grams. Given a scale that provides an exact measurement, how
would you find the heavy bottle? You can only use the scale once.
Complexity: O(N)
Usage: the_heavy_pill <bottles>
'''

# libraries
import random


# function
def answer(n):

    # generate bottle numbers
    bottles = [x+1 for x in range(n)]

    # get expected sum
    expected = sum(bottles)

    # seed large pill
    heavypill = random.randint(0, n-1)

    # fill bottles
    bottles[heavypill] *= 1.1

    # get actual sum
    actual = sum(bottles)

    # exit
    return (actual - expected) / 0.1


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # run
    print answer(int(args['<bottles>']))
