"""
K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k
 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Example 4:

Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2
Example 5:

Input: nums = [-1,-2,-3], k = 1
Output: 2

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
"""

from typing import List

class Solution1:
    def findPairs(self, nums: List[int], k: int) -> int:
        def binary_search(nums, l, r, key):
            if l <= r:
                mid = (l + r) // 2
                if nums[mid] == key:
                    return mid
                elif nums[mid] < key:
                    return binary_search(nums, mid+1, r, key)
                else:
                    return binary_search(nums, l, mid-1, key)
            return -1

        n = len(nums)
        if n <= 1:
            return 0
        nums = sorted(nums)
        if nums[-1] - nums[0] < k:
            return 0
        res = []
        count = 0
        prev_start_val = set()
        for idx, val in enumerate(nums):
            if val in prev_start_val:
                continue
            key = val + k
            if binary_search(nums, idx+1, n-1, key) > idx:
                res.append((val, key))
                count += 1
            prev_start_val.add(val)
        return count


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        if k == 0:
            hash_set = {}
            for n in nums:
                hash_set[n] = hash_set.get(n, 0) + 1
            return len([n for n in hash_set if hash_set[n] > 1])
        s = set(nums)
        if len(s) == 1:
            return 1
        count = 0
        for n in s:
            if n+k in s:
                count += 1
        return count



print(Solution().findPairs([1,3,1,5,4], 0) == 1)
print(Solution().findPairs([3,1,4,1,5], 2)==2)
print(Solution().findPairs([1,2,3,4,5], 1) == 4)
print(Solution().findPairs([1,2,4,4,3,3,0,9,2,3], 3) == 2)
print(Solution().findPairs([-1,-2,-3], 1) == 2)
print(Solution().findPairs([3,1,4,1,5], 2) == 2)
print(Solution().findPairs([0,0,0], 0)==1)







