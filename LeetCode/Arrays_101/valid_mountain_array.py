"""
Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Input: arr = [2,1]
Output: false

Input: arr = [3,5,5]
Output: false

Input: arr = [0,3,2,1]
Output: true

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        l = 0
        r = len(arr)-1
        l_val = -1
        r_val = -1
        while l < len(arr) and arr[l] > l_val:
                l_val = arr[l]
                l += 1
        if l == len(arr):
            return False
        while r >= l and arr[r] > r_val:
                r_val = arr[r]
                r -= 1
        if r == 0:
            return False
        if abs(l-r) > 1:
            return False
        if l == r:
            return arr[l-1] < arr[l] and arr[r+1] > arr[r]
        else:
            return (arr[l-1] < arr[l] and arr[l] > arr[r]) or (arr[l] < arr[r] and arr[r] > arr[r+1])
arr = [2,1]
print(Solution().validMountainArray(arr))

arr = [3,5,5]
print(Solution().validMountainArray(arr))

arr = [0,3,2,1]
print(Solution().validMountainArray(arr))

arr = [0,3,-1, 2,1]
print(Solution().validMountainArray(arr))

arr = [0,3,4, 2,1]
print(Solution().validMountainArray(arr))

arr = [0,1,2,3,4,8,9,10,11,12,11]
print(Solution().validMountainArray(arr))

arr = [10,11,12,11, 10, 9, 8, 7, 6, 5, 4]
print(Solution().validMountainArray(arr))

arr = [0,1,2,3,4,5,6,7,8,9]
print(Solution().validMountainArray(arr))

arr = [9,8,7,6,5,4,3,2,1]
print(Solution().validMountainArray(arr))

arr = [3,6,5,6,7,6,5,3,0]
print(Solution().validMountainArray(arr))






