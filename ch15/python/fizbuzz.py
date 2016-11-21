#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    In the classic problem FizzBuzz, you are told to print the numbers from 1
to n. However, when the number is divisible by 3, print "Fizz". When it is
divisible by 5, print "Buzz." When it is divisble by 3 and 5, print "FizzBuzz".
In this problem, you are asked to do this in a multithreaded way. Implement a
multithreaded version of FizzBuzz with four threads. One thread checks for
divisibility of 3 and prints "Fizz". Another thread is responsible for
divisibility of 5 and prints "Buzz". A third thread is responsible for
divisibility of 3 and 5 and prints "FizzBuzz". A fourth thread does the
numbers.
Complexity: TODO
Usage: fizzbuzz <int>
'''

# libraries
import thread


# decorator
def decorator(words):
    '''
    Decorator for wrapping.
    '''
    # decorator function
    def thread_print(boolean):
        '''
        Function to print thread specific output.
        '''
        print words

    # return function
    return thread_print


# function
def answer(n):

    # generating functions
    fizz = decorator('fizz')
    buzz = decorator('buzz')
    fizzbuzz = decorator('fizzbuzz')

    # iterate from
    for i in range(1, n+1):

        # calculate
        three = not i % 3
        five = not i % 5

        # fizz buzz
        if three and five:
            fizzbuzz(five and three)
        elif three:
            fizz(three)
        elif five:
            buzz(five)
        else:
            print i


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # run
    answer(int(args['<int>']))
