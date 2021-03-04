"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000

"""
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        n = len(A)
        decreasing = True
        increasing = True
        for i in range(n-1):
            if A[i] > A[i+1]:
                decreasing = False
            if A[i] < A[i+1]:
                increasing = False
        return decreasing or increasing

nums = [2, 2, 2, 1, 4, 5]
print(Solution().isMonotonic(nums))

nums = [1, 2, 2, 3]
print(Solution().isMonotonic(nums))

nums = [9, 7, 5, 3]
print(Solution().isMonotonic(nums))

nums = [1, 6, 5, 4, 8, 3]
print(Solution().isMonotonic(nums))

nums = [2, 2, 2, 2]
print(Solution().isMonotonic(nums))

nums = [2]
print(Solution().isMonotonic(nums))

nums = [1, 2]
print(Solution().isMonotonic(nums))

nums = [9, 6]
print(Solution().isMonotonic(nums))


