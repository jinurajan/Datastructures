"""
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, . 
The second line contains an integer, .

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0 
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first  letters of the infinite string are a, we print  on a new line.

"""

#!/bin/python

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    a_count_in_s = 0
    remaining_a_count = 0

    # find a's in the unique s string
    for i in range(len(s)):
        if s[i] == 'a':
            a_count_in_s += 1

    number_of_s_in_n = n // len(s)

    count_in_n = number_of_s_in_n * a_count_in_s

    remainder = n % len(s)

    for i in range(remainder):
        if s[i] == 'a':
            remaining_a_count += 1

    return count_in_n + remaining_a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
