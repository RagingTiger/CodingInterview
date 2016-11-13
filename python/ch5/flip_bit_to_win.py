#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    You have an integer you can flip exactly one bit from a 0 to a 1. Write
code to find the length of the longest sequence of 1s you could create.
EXAMPLE
Input:    1775   (or: 11011101111)
Output:   8
Complexity: O(N)
Usage: flip_bit_to_win <integer>
'''


# function
def answer(n):

    # convert int to bit string
    bitstring = bin(n).split('b')[1]

    # then cut out '0'
    bitlist = bitstring.split('0')

    # now measure
    bllen = len(bitlist)
    longest = 0
    for i, bitgroup in enumerate(bitlist):
        if bitgroup is not '':
            l1 = len(bitgroup)
            if ((i+1) % bllen) != 0:
                if bitlist[i+1] is not '':
                    l2 = len(bitlist[i+1])
                    newseq = l1 + l2 + 1
                    if longest < newseq:
                        longest = newseq
                        continue
            newseq = l1 + 1
            if longest < newseq:
                longest = newseq

    # return
    print longest
    return bitstring


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # return
    print answer(int(args['<integer>']))
