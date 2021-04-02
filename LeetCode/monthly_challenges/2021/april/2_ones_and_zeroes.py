"""
Ones and Zeroes

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.



Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.


Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""
from typing import List

from collections import Counter

class Solution1:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = {}

        def calculate(i, zeroes, ones):
            if i == len(strs):
                return 0
            if (i, zeroes, ones) in mem:
                return mem[(i, zeroes, ones)]
            count = Counter(strs[i])
            taken = -1
            if zeroes - count['0'] >= 0 and ones - count['1'] >= 0:
                taken = calculate(i + 1, zeroes - count['0'], ones - count['1']) + 1
            not_taken = calculate(i + 1, zeroes, ones)
            mem[(i, zeroes, ones)] = max(taken, not_taken)
            return mem[(i, zeroes, ones)]

        return calculate(0, m, n)


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for s in strs:
            count = Counter(s)
            zeros , ones = count['0'], count[1]
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(1 + dp[i - zeros][j - ones], dp[i][j])
        return dp[m][n]


strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(Solution().findMaxForm(strs, m, n))
strs = ["10","0","1"]
m = 1
n = 1
print(Solution().findMaxForm(strs, m, n))