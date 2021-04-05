"""
 Global and Local Inversions

 We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.

"""


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i - x) <= 1 for i, x in enumerate(A))

class Solution1(object):
    def isIdealPermutation(self, A):
        N = len(A)
        floor = N
        for i in xrange(N-1, -1, -1):
            floor = min(floor, A[i])
            if i >= 2 and A[i-2] > floor:
                return False
        return True

class Solution2(object):
    def isIdealPermutation(self, A):
        return all(x < A[j]
                   for i, x in enumerate(A)
                   for j in xrange(i+2, len(A)))

