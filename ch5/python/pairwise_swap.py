#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Write a program to swap odd and even bits in an integer with as few
instructions as possible (e.g. bit 0 and bit 1 are swapped, bit 2 and bit 3 are
swapped, and so on).
Complexity: TODO
Usage: pairwise_swap <N>
'''

# libraries
import sys


def answer(integer):
    '''
    Function to flip bits.
    '''
    # get bit length of max int
    bitlen = len(bin(sys.maxint).split('b')[1]) + 1

    # generate bitmasks
    evenmask = int(''.join([str(i % 2) for i in range(bitlen)]), 2)
    oddmask = int(''.join([str(i % 2) for i in range(1, bitlen+1)]), 2)

    # extract odd and even bits
    evenbits = integer & evenmask
    oddbits = integer & oddmask

    # shift even left / odd right
    evenbits = evenbits << 1
    oddbits = oddbits >> 1

    # combine bits for flipping odd/even
    flippedbits = evenbits | oddbits

    # exit
    return flippedbits


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # run
    flip = answer(int(args['<N>']))
    print 'N as int   : {0}'.format(int(args['<N>']))
    print 'Flip as int: {0}'.format(flip)
    print 'N as bin   : {0}'.format(bin(int(args['<N>'])))
    print 'Flip as bin: {0}'.format(bin(flip))
