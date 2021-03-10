"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.



Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000


Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result = []
        carry = 0
        start = len(A) - 1
        K = list(str(K))
        k_start = len(K)-1
        max_len = max(len(A), len(K)) - 1
        while max_len >= 0:
            val_1 = 0 if start < 0 else A[start]
            val_2 = 0 if k_start < 0 else int(K[k_start])
            s = val_1 + val_2 + carry
            if s >= 10:
                carry = 1
                s = s % 10
            else:
                carry = 0
            result.append(s)
            start -= 1
            k_start -= 1
            max_len -= 1
        if carry:
            result.append(carry)
        return result[::-1]



A = [0]
K = 10000

print(Solution().addToArrayForm(A, K))