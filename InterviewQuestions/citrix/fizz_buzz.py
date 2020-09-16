#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n + 1):
        three_mode = i % 3
        five_mode = i % 5
        if three_mode == 0 and five_mode == 0:
            print 'FizzBuzz'
        elif three_mode == 0 and five_mode != 0:
            print 'Fizz'
        elif three_mode != 0 and five_mode == 0:
            print 'Buzz'
        else:
                print i

if __name__ == '__main__':
    fizzBuzz(15)