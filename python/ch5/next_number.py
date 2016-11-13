#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given a positive integer, print the next smallest and the next largest
number that have the same number of 1 bits in their binary representation.
Complexity: O(N)
Usage: nex_number <int>
'''


def answer(n):

    # get bit string
    bitstring = bin(n).split('b')[1]

    # get original length
    origlen = len(bitstring)

    # get next largest
    ones = ''.join(bitstring.split('0'))
    zeros = ''.join(['0' for x in range(origlen - len(ones))])
    largest = int(ones+zeros, 2)

    # get bitlist
    bitlist = list(bitstring)

    # find index and swap '0' and '1'
    for i in range(origlen, 0, -1):
        if bitlist[i-1] is '1':
            for j in range(i-1, 0, -1):
                if bitlist[j-1] is '0':
                    bitlist[j-1] = '1'
                    bitlist[i-1] = '0'
                    break
            break

    # get next smallest
    smallest = int(''.join(bitlist), 2)

    # return values
    return largest, smallest


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # run
    print answer(int(args['<int>']))
