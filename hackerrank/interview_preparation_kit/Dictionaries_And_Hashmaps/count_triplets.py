"""
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

For example, . If , we have  and  at indices  and .

Function Description

Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given  as an integer.

countTriplets has the following parameter(s):

arr: an array of integers
r: an integer, the common ratio
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio. 
The next line contains  space-seperated integers .

Constraints

Output Format

Return the count of triplets that form a geometric progression.

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2
Explanation 0

There are  triplets in satisfying our criteria, whose indices are  and 

Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
Explanation 1

The triplets satisfying are index , , , ,  and .

Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4
Explanation 2

The triplets satisfying are index , , , .
"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
	temp = arr[0]
	triplets = []
	j = 1

	while j in len(arr):






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = raw_input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = map(long, raw_input().rstrip().split())

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
