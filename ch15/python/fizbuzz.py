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
import threading


# closure
def threading_closure(word):
    '''
    Closure for wrapping.
    '''
    # results
    def thread_results():
        print word

    # closed over function
    def thread_execute():
        '''
        Function to print thread specific output.
        '''
        t = threading.Thread(target=thread_results)
        t.start()
        t.join()

    # return function
    return thread_execute


# function
def answer(n):

    # generating functions
    threads = {}
    for name in ['fizz', 'buzz', 'fizzbuzz']:
        threads[name] = threading_closure(name)

    # iterate from
    for i in range(1, n+1):

        # calculate
        three = not i % 3
        five = not i % 5

        # fizz buzz
        if three and five:
            threads['fizzbuzz']()
        elif three:
            threads['fizz']()
        elif five:
            threads['buzz']()
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
